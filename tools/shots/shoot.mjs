// Capture review screenshots of the site with the locally installed Chrome.
// Usage: node shoot.mjs [url] [outDir]
// Defaults: http://localhost:8124/ and ../../.impeccable/review
import puppeteer from 'puppeteer-core';
import { mkdirSync } from 'node:fs';
import { resolve } from 'node:path';

const url = process.argv[2] || 'http://localhost:8124/';
const out = resolve(process.argv[3] || new URL('../../.impeccable/review', import.meta.url).pathname);
mkdirSync(out, { recursive: true });

const browser = await puppeteer.launch({
  executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  headless: true,
  protocolTimeout: 60000,
  args: ['--hide-scrollbars'],
});
const wait = (ms) => new Promise((r) => setTimeout(r, ms));

async function open(width, height, { reduced = false, mobile = false } = {}) {
  const page = await browser.newPage();
  await page.setViewport({ width, height, deviceScaleFactor: 1, isMobile: mobile, hasTouch: mobile });
  await page.emulateMediaFeatures([{ name: 'prefers-reduced-motion', value: reduced ? 'reduce' : 'no-preference' }]);
  await page.goto(url, { waitUntil: 'load', timeout: 60000 });
  await page.evaluate(() => document.fonts.ready);
  return page;
}

// Scroll through the page so scroll-triggered ink passes run, then return to top.
async function settle(page) {
  await page.evaluate(async () => {
    const step = innerHeight * 0.6;
    for (let y = 0; y < document.body.scrollHeight; y += step) {
      window.scrollTo({ top: y, behavior: 'instant' });
      await new Promise((r) => setTimeout(r, 120));
    }
    window.scrollTo({ top: 0, behavior: 'instant' });
  });
  await wait(1800);
}

const shots = [];
async function full(name, width, height, opts) {
  const page = await open(width, height, opts);
  await settle(page);
  // the fixed dock would paint mid-page in a full-page capture; state-mobile-dock.png covers it
  await page.evaluate(() => { const d = document.querySelector('.dock'); if (d) d.style.display = 'none'; });
  const file = `${out}/${name}.png`;
  await page.screenshot({ path: file, fullPage: true });
  const overflow = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
  shots.push({ file, width, overflow });
  await page.close();
}

await full('desktop', 1440, 900);
await full('laptop-1024', 1024, 768);
await full('tablet-768', 768, 1024, { mobile: true });
await full('mobile', 390, 844, { mobile: true });
await full('mobile-320', 320, 640, { mobile: true });
await full('desktop-reduced-motion', 1440, 900, { reduced: true });

// First viewport only, at rest and mid-animation (proves nothing is ever blank).
{
  const page = await browser.newPage();
  await page.setViewport({ width: 1440, height: 900 });
  await page.goto(url, { waitUntil: 'domcontentloaded' });
  await wait(120);
  await page.screenshot({ path: `${out}/first-viewport-early.png` });
  await wait(2000);
  await page.screenshot({ path: `${out}/first-viewport.png` });
  shots.push({ file: `${out}/first-viewport-early.png` }, { file: `${out}/first-viewport.png` });
  await page.close();
}

// Interaction states.
{
  const page = await open(1440, 900);
  await page.evaluate(() => window.scrollTo(0, 0));
  await wait(400);
  await page.hover('.door-give');
  await wait(400);
  await page.screenshot({ path: `${out}/state-hover-give.png` });
  await page.keyboard.press('Tab');
  await wait(200);
  await page.screenshot({ path: `${out}/state-focus-skip-link.png` });
  shots.push({ file: 'state-*.png (2 files)' });
  await page.close();
}
{
  const page = await open(390, 844, { mobile: true });
  await page.evaluate(() => window.scrollTo({ top: document.getElementById('give').offsetTop, behavior: 'instant' }));
  await wait(1600);
  await page.screenshot({ path: `${out}/state-mobile-dock.png` });
  shots.push({ file: `${out}/state-mobile-dock.png` });
  await page.close();
}

await browser.close();
console.log(JSON.stringify(shots, null, 1));
