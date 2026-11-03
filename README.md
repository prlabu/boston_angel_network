# Boston Angel Network website

The public website for Boston Angel Network Inc. (501(c)(3), EIN 41-4383401), which hosts the Boston Angel Fund. It's one static page with no build step, no framework, no cookies, no analytics and no third-party requests. The only things that leave the site are the visitor's own clicks to Chuffed, LUCE and BIJAN.

## What's in this folder

| Path | What it is | Publish it? |
|---|---|---|
| `site/` | **The website.** The deploy workflow publishes this folder and nothing else. | **Yes** |
| `site/index.html` | The page. All copy lives here. | |
| `site/css/site.css`, `site/js/site.js` | Styles and the small script for motion, copy/share, the nav marker and the phone bar. The page works with JavaScript off. | |
| `site/assets/` | Logo SVGs, favicons, share image. | |
| `site/fonts/` | League Gothic and Atkinson Hyperlegible (WOFF2) plus their OFL licences. | |
| `site/_headers` | Security and cache headers for Netlify or Cloudflare Pages. | |
| `design-source/` | The logo image the SVG was traced from, and its provenance. Kept on the local computer, not in the repo. | No |
| `tools/` | Scripts to deploy and to rebuild the fonts, logo trace, share image and review screenshots. | No |
| `DESIGN.md` | The design system: inks, type, components, motion. | No |
| `PRODUCT.md`, `SITE_PLAN.md` | Product facts and the build plan. Kept on the local computer, not in the repo. | No |
| `.github/workflows/deploy.yml` | Publishes `site/` to GitHub Pages on every push to `main`. | No |
| `.impeccable/` | Design working files: direction brief, sketches, review screenshots. Kept on the local computer, not in the repo. | No |

## Preview locally

```bash
python3 -m http.server 8124 --directory site
```

Then open http://localhost:8124.

## Edit the copy

Open `site/index.html` in any text editor. The sections, top to bottom:

1. **Hero:** the `<h1>` headline, the lede, and the two doors: *Give to the fund* and *Need help with legal fees?*
2. **How we can help** (`id="help"`): the three steps, the LUCE hotline box, and "Where we fit" (the medium description from Zahra's doc).
3. **Give** (`id="give"`): the three facts, the kickoff goal, and the Donate and Share buttons.
4. **Footer** (`id="contact"`): the organization line, contact, and the groups we stand alongside.

The copy follows Zahra's doc "10.31.2026 External Communications Drafts". The lede is its short description; "Where we fit" is its medium description. Three facts are corrected against the sources: LUCE's line is the "LUCE Defense Hotline"; LUCE points supporters to Operation Milkweed rather than coordinating it; the bond fund is the "Beyond Bond & Legal Defense Fund", which BIJAN started and which is now its own 501(c)(3). Per a BIJAN representative (Nov 2026), describe it as bond support that contributes toward bond payments, never as paying bonds outright: bonds have grown too large to promise that.

Leave the long `<path d="…">` blocks alone: they're the logo.

When the fundraising goal changes, update `$1,000` in the hero's Give door and in the Give section. Then rebuild the share image:

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --hide-scrollbars --allow-file-access-from-files --window-size=1200,630 --screenshot=site/assets/og-image.png "file://$PWD/tools/og/og.html"
```

## Deploy (GitHub Pages)

The site deploys automatically. Every push to `main` runs `.github/workflows/deploy.yml`, which:

1. copies `site/`;
2. runs `tools/deploy/prepare.py` to point the share image, canonical link and 404 page at the live address;
3. publishes the result to GitHub Pages.

Only `site/` is published.

- **Live address:** https://saifiz2.github.io/boston_angel_fund/
- **First-time setup** (done once): in the repo, go to *Settings → Pages → Build and deployment* and set *Source* to **GitHub Actions**. The repo is public, so Pages works on the free plan.
- **Check a deploy:** open the repo's *Actions* tab. Each push shows a "Deploy site" run with a link to the live page.

GitHub Pages can't send custom headers, so `site/_headers` isn't used there. The Content-Security-Policy still applies through the `<meta>` tag in `index.html`, and github.io sends HSTS. `_headers` only takes effect if the site ever moves to Netlify or Cloudflare Pages.

### Custom domain

1. Add the domain in *Settings → Pages → Custom domain* and turn on *Enforce HTTPS*.
2. Create the DNS records GitHub shows you.

The deploy workflow picks up the new address by itself: share links, the canonical URL and the 404 page all follow it.

## Before launch

**Brand and copy (Zahra):**

- [ ] Compare the traced logo with Zahra's original `OPTION B.png`. The SVG was traced on 2026-11-01 from the Chuffed campaign image, which is kept outside the repo with its provenance notes.
- [ ] Approve the copy, especially the help steps: what to include in a first email, "Writing for someone else, like a detained friend or relative? That’s fine.", and "We’ll reply, ask a few questions, and tell you whether the fund can help." Also confirm who qualifies and what the fund covers. Once a response time is set, add it to step 2.
- [ ] The site uses the doc's "We stand alongside…" rather than "partners". If LUCE and BIJAN agree to be called partners, those lines can say so.

**Chuffed:**

- [ ] Turn on tax-deductible receipts: *Organisation Setup* → "Are you a Registered Charity…" → enter EIN 41-4383401. Check the receipt names Boston Angel Network.
- [ ] Check the campaign's fee model. The site makes no "100% goes to the fund" claim; keep it that way unless the campaign is on "Keep 100%".

**Legal and compliance:**

- [ ] Massachusetts: public charities generally must register with the Attorney General's Non-Profit/Public Charities Division and hold a Certificate of Solicitation before asking for donations (https://www.mass.gov/info-details/registering-a-public-charity). Confirm this is done. It was flagged in research but not verified for this organization.

**Partners and privacy:**

- [ ] Re-check the LUCE Defense Hotline (617-370-5023, call or text, 6am–9pm daily) at https://www.lucemass.org/ shortly before launch, and consider telling LUCE and BIJAN they're named.
- [ ] The IRS record lists a residential address. It's not on the site; change it with Form 8822-B if needed.

## Rebuilding things

- **Fonts:** see `tools/fonts/README.md`. `build.py` re-creates the subsetted WOFF2 files from the OFL sources in `tools/fonts/src/`.
- **Logo:** `bash tools/logo/final.sh path/to/logo-source.jpg` re-traces the logo (setup steps are at the top of the script). The SVGs in `site/assets/` use `fill="currentColor"`, so CSS sets the ink color.
- **Review screenshots:** run `cd tools/shots && npm install && node shoot.mjs` with the local server running.

## Licences and credits

- League Gothic and Atkinson Hyperlegible: SIL Open Font License 1.1 (licence files in `site/fonts/`).
- Logo: designed for Boston Angel Network; vector trace made 2026-11-01.
