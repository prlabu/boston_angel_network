---
name: Boston Angel Fund
description: A two-ink organizing zine for a community legal-fee fund. Riso blue and sunflower on copier paper.
colors:
  blue: "#3255A4"
  sunflower: "#FFB511"
  overprint: "#2E3A10"
  paper: "#FBFAF6"
typography:
  display:
    fontFamily: "League Gothic, Arial Narrow, sans-serif"
    fontSize: "clamp(3.2rem, 6.4vw, 5.25rem)"
    fontWeight: 400
    lineHeight: 0.9
    letterSpacing: "0.01em"
  headline:
    fontFamily: "League Gothic, Arial Narrow, sans-serif"
    fontSize: "clamp(2.8rem, 6vw, 4.6rem)"
    fontWeight: 400
    lineHeight: 0.9
    letterSpacing: "0.01em"
  door-headline:
    fontFamily: "League Gothic, Arial Narrow, sans-serif"
    fontSize: "clamp(2.6rem, 4.6vw, 3.9rem)"
    fontWeight: 400
    lineHeight: 0.9
    letterSpacing: "0.01em"
  numeral:
    fontFamily: "League Gothic, Arial Narrow, sans-serif"
    fontSize: "6rem"
    fontWeight: 400
    lineHeight: 1
  figure:
    fontFamily: "League Gothic, Arial Narrow, sans-serif"
    fontSize: "clamp(4rem, 8vw, 6rem)"
    fontWeight: 400
    lineHeight: 0.9
  title:
    fontFamily: "League Gothic, Arial Narrow, sans-serif"
    fontSize: "2.3rem"
    fontWeight: 400
    lineHeight: 1
  title-urgent:
    fontFamily: "League Gothic, Arial Narrow, sans-serif"
    fontSize: "1.9rem"
    fontWeight: 400
    lineHeight: 1
  title-footer:
    fontFamily: "League Gothic, Arial Narrow, sans-serif"
    fontSize: "1.6rem"
    fontWeight: 400
    lineHeight: 1
  lede:
    fontFamily: "Atkinson Hyperlegible, system-ui, sans-serif"
    fontSize: "clamp(1.15rem, 1.6vw, 1.35rem)"
    fontWeight: 400
    lineHeight: 1.55
  intro:
    fontFamily: "Atkinson Hyperlegible, system-ui, sans-serif"
    fontSize: "1.2rem"
    fontWeight: 400
    lineHeight: 1.55
  body:
    fontFamily: "Atkinson Hyperlegible, system-ui, sans-serif"
    fontSize: "1.125rem"
    fontWeight: 400
    lineHeight: 1.55
  small:
    fontFamily: "Atkinson Hyperlegible, system-ui, sans-serif"
    fontSize: "0.95rem"
    fontWeight: 400
    lineHeight: 1.55
  nav:
    fontFamily: "Atkinson Hyperlegible, system-ui, sans-serif"
    fontSize: "0.95rem"
    fontWeight: 700
    lineHeight: 1.55
  button:
    fontFamily: "Atkinson Hyperlegible, system-ui, sans-serif"
    fontSize: "1.05rem"
    fontWeight: 700
    lineHeight: 1
  button-small:
    fontFamily: "Atkinson Hyperlegible, system-ui, sans-serif"
    fontSize: "0.95rem"
    fontWeight: 700
    lineHeight: 1
rounded:
  square: "0px"
spacing:
  gutter: "clamp(20px, 4vw, 56px)"
  section: "clamp(56px, 8vw, 112px)"
  column-gap: "clamp(32px, 5vw, 72px)"
  steps-gap: "clamp(24px, 3vw, 48px)"
  door: "clamp(24px, 3vw, 36px)"
  give-box: "clamp(24px, 3vw, 40px)"
  urgent: "20px 24px"
  row: "12px"
components:
  button:
    backgroundColor: "transparent"
    textColor: "{colors.blue}"
    typography: "{typography.button}"
    rounded: "{rounded.square}"
    padding: "0.85em 1.2em"
    height: "48px"
  button-small:
    typography: "{typography.button-small}"
    rounded: "{rounded.square}"
    padding: "0.6em 0.95em"
    height: "44px"
  button-blue:
    backgroundColor: "{colors.blue}"
    textColor: "{colors.paper}"
    typography: "{typography.button}"
    rounded: "{rounded.square}"
  button-sun:
    backgroundColor: "{colors.sunflower}"
    textColor: "{colors.overprint}"
    typography: "{typography.button}"
    rounded: "{rounded.square}"
  button-paper:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.blue}"
    typography: "{typography.button}"
    rounded: "{rounded.square}"
  button-on-sunflower:
    backgroundColor: "transparent"
    textColor: "{colors.overprint}"
    typography: "{typography.button}"
    rounded: "{rounded.square}"
  button-done:
    backgroundColor: "{colors.sunflower}"
    textColor: "{colors.overprint}"
  door-give:
    backgroundColor: "{colors.sunflower}"
    textColor: "{colors.blue}"
    typography: "{typography.door-headline}"
    rounded: "{rounded.square}"
    padding: "{spacing.door}"
  door-give-copy:
    textColor: "{colors.overprint}"
    typography: "{typography.body}"
  door-help:
    backgroundColor: "{colors.blue}"
    textColor: "{colors.paper}"
    typography: "{typography.door-headline}"
    rounded: "{rounded.square}"
    padding: "{spacing.door}"
  give-box:
    backgroundColor: "{colors.sunflower}"
    textColor: "{colors.overprint}"
    rounded: "{rounded.square}"
    padding: "{spacing.give-box}"
  give-box-goal:
    textColor: "{colors.blue}"
    typography: "{typography.figure}"
  step-number:
    textColor: "{colors.blue}"
    typography: "{typography.numeral}"
  step-title:
    textColor: "{colors.blue}"
    typography: "{typography.title}"
  urgent-note:
    textColor: "{colors.blue}"
    rounded: "{rounded.square}"
    padding: "{spacing.urgent}"
  site-header:
    backgroundColor: "{colors.paper}"
    height: "68px"
  nav-link:
    textColor: "{colors.blue}"
    typography: "{typography.nav}"
  dock:
    backgroundColor: "{colors.paper}"
    padding: "12px 16px"
  skip-link:
    backgroundColor: "{colors.blue}"
    textColor: "{colors.paper}"
    padding: "0.7em 1em"
---

# Design System: Boston Angel Fund

## Overview

**Creative North Star: "The Two-Ink Organizing Zine"**

The site is printed, not designed: a flyer that neighbors run off on a two-drum risograph and pass along, trusted because the community made it. Every surface is built from two inks on copier paper. Riso blue carries the words. Sunflower carries emphasis and the act of giving. Where the two plates cross, they make a third, darker tone, the overprint, which is a printing fact and not a third colour. The paper has a faint copier grain, rules are 3px strokes of blue, and every block of ink is square.

Density is low and the voice is loud only where it counts. Tall condensed capitals (League Gothic) name things; a highly legible humanist sans (Atkinson Hyperlegible) says everything a person reads in sentences. The page offers exactly two doors from the first screen, one to give and one to get help, and keeps both within reach at every width.

The system refuses the nonprofit template: no hero photograph, no stock or enforcement imagery, no rows of identical icon cards, no stat counters, no labels stacked above headings. Its one authored moment is the print run on load, where the plates settle into registration and the logo's wings spread. Words never fade or move out of reach; only ink is ever undrawn.

**Key Characteristics:**
- Two inks (blue, sunflower) on grained copier paper; overprint appears only where they cross.
- Small text on sunflower always prints in overprint.
- League Gothic caps for names and numbers, Atkinson Hyperlegible for every sentence.
- Square ink blocks, 3px solid rules, one dashed rule for urgent outside help.
- Flat at rest; hover lifts only on pointers that can hover.
- One authored motion: the print run. Reduced-motion and forced-colors paths are first-class.

## Colors

Two riso inks on copier paper, plus the tone they make together.

### Primary
- **Riso Medium Blue** (#3255A4): the text ink. All running text, every heading on paper, rules, borders of outline buttons, the focus ring, icons and the logo. It also fills the Need-help door, blue buttons and the skip link, where paper-coloured text reads out of it.

### Secondary
- **Sunflower** (#FFB511): the emphasis ink. It fills the Give door, the Give box, sunflower buttons and the copied/shared confirmation state, and prints as bands: the highlight over "Boston’s" in the headline, the passes over the step numbers, and the marker under the current nav link. It is never a text colour on paper (1.7:1).

### Tertiary
- **Overprint** (#2E3A10): what blue looks like printed over sunflower. Used for every small text on sunflower (door copy, button labels, the goal label, the Share button's border and label) and for text selection. Multiply bands produce the same tone on their own: blue letters under a sunflower band render near #323C0B.

### Neutral
- **Copier Paper** (#FBFAF6): the page, the sticky header, the phone dock, and text on blue. The body background adds a 160px tile of fractal-noise grain, tinted blue at 6% alpha, so the rendered paper reads close to #F6F6F4.

### Contrast roles

| Pair | Ratio | Where it is used |
|---|---|---|
| Blue on paper | 6.8:1 (6.5:1 on the grained paper) | All text on paper |
| Paper on blue | 6.8:1 | Need-help door, blue buttons, skip link |
| Overprint on sunflower | 6.9:1 | All small text on sunflower |
| Multiply overprint on sunflower | 6.6:1 | "Boston’s" and the step numerals under their bands |
| Blue on sunflower | 4.0:1 | Display type only: the Give door headline (41.6px and up) and the goal figure (64px and up) |
| Sunflower focus ring on blue | 4.0:1 | Focus inside the Need-help door |
| Sunflower on paper | 1.7:1 | Never text. Fills and bands only, always carrying overprint or blue type |

### Named Rules

**The Two Plates Rule.** The page prints with blue and sunflower only, on paper. Overprint is the result of the two crossing, not a third ink. No other hues, no tints, no visible gradients.

**The Overprint Rule.** Small text on sunflower prints in overprint (#2E3A10). Blue on sunflower is allowed only at display size, where 4.0:1 clears the large-text threshold.

**The Ink Over Letters Rule.** Highlight bands print over the letters, not behind them: a sunflower pseudo-element above the text with `mix-blend-mode: multiply`, inside an isolated stacking context, so the crossed letters turn overprint.

## Typography

**Display Font:** League Gothic (with Arial Narrow, sans-serif)
**Body Font:** Atkinson Hyperlegible (with system-ui, sans-serif)

**Character:** A poster face and a reading face. League Gothic is narrow, loud and always in capitals, the voice of a stencilled flyer; Atkinson Hyperlegible was drawn for low-vision readers, so its distinct letterforms (including its slashed zero) carry the help path for someone reading under stress, on a phone, or in a second language.

Both faces are self-hosted WOFF2 files, subset to Latin (U+0000–017F plus punctuation and symbols), loaded with `font-display: swap`. League Gothic and regular Atkinson are preloaded; Atkinson Bold sets buttons, nav and emphasis. League Gothic carries `font-synthesis: none` so no fake bold or italic appears.

### Hierarchy
- **Display** (League Gothic 400, clamp(3.2rem, 6.4vw, 5.25rem), 0.9, +0.01em, caps): the hero headline only, set as four fixed lines.
- **Headline** (League Gothic 400, clamp(2.8rem, 6vw, 4.6rem), 0.9, caps, max 24ch): section titles.
- **Door headline** (League Gothic 400, clamp(2.6rem, 4.6vw, 3.9rem), 0.9, caps): the two hero doors.
- **Numeral** (League Gothic 400, 6rem, 1): the step numbers.
- **Figure** (League Gothic 400, clamp(4rem, 8vw, 6rem), 0.9): the fundraising goal.
- **Title** (League Gothic 400, 2.3rem, 1, caps): step titles and "Where we fit". Urgent-note title at 1.9rem; footer column titles at 1.6rem.
- **Lede** (Atkinson 400, clamp(1.15rem, 1.6vw, 1.35rem), 1.55, max 36ch): the hero's one sentence.
- **Intro** (Atkinson 400, 1.2rem, 1.55, max 62ch): the sentence under a section title.
- **Body** (Atkinson 400, 1.125rem (18px), 1.55): everything else. Measures run 32 to 52ch by component.
- **Small** (Atkinson 400, 0.95rem, 1.55, max 70ch): plain email addresses, small print.
- **Label** (Atkinson 700, 1.05rem buttons, 0.95rem small buttons and nav, line-height 1): sentence case, never tracked caps.

### Named Rules

**The 6rem Ceiling Rule.** No type on the site exceeds 6rem (96px). The numerals, the goal figure and the 404 headline sit at the ceiling; the hero headline stops at 5.25rem.

**The Caps Are Names Rule.** League Gothic is always uppercase and only names things: headings, numerals, the goal. Sentences, labels and buttons are Atkinson in sentence case.

**The Curly Quotes Rule.** Visible copy uses typographic apostrophes and quotes (’ “ ”) and en dashes for ranges (6am–9pm). Headings use `text-wrap: balance`, paragraphs `text-wrap: pretty`, and short tokens that must not break (501(c)(3), the EIN, phone numbers, "Boston area") are wrapped in no-break spans.

## Layout

A single page of anchored sections inside one container: max 1240px, centred, with a fluid gutter (clamp(20px, 4vw, 56px)). Every section opens with a full-width 3px blue rule and clamp(56px, 8vw, 112px) of block padding. The sticky header is 68px tall, and `scroll-padding-top: 68px` lands each section's top rule exactly on the header's rule when a nav link is followed.

Wide-screen grids:
- **Hero:** 1.35fr | 1fr, gap clamp(32px, 5vw, 72px). Left: logo, headline, lede. Right: the two doors stacked with clamp(28px, 4vw, 48px) between them, vertically centred.
- **Steps:** three equal columns, gap clamp(24px, 3vw, 48px).
- **Where we fit:** minmax(12ch, 1fr) | 3fr, title left, text right.
- **Give:** 1.2fr | 1fr, bottom-aligned so the Give box sits level with the end of the facts.
- **Footer:** 1.3fr | 1fr | 1fr.

**The 53.75em breakpoint.** At max-width 53.75em (860px at default text size) every grid collapses to one column, the header nav and header Donate button hide, and the phone dock takes over. The breakpoint is in em so a reader with a larger default font gets the phone layout sooner. On phones in landscape (max-height 500px) the header stops sticking so content keeps the screen. `scroll-padding-bottom: 96px` on phones keeps focused controls clear of the dock. Nothing scrolls horizontally down to 320px.

## Elevation & Depth

Flat print. Depth comes from ink layering, not light: sunflower bands multiply over blue letters, the Give door's sunflower plate sits under its type, and the sticky header separates itself with a 3px rule, not a shadow. Nothing has a shadow at rest.

### Shadow Vocabulary
- **Button lift** (`box-shadow: 0 8px 18px -6px rgba(50, 85, 164, .45)`): hover on a button, with a 2px rise.
- **Button press** (`box-shadow: 0 2px 6px -2px rgba(50, 85, 164, .4)`): active state, back to the baseline.
- **Door lift** (`box-shadow: 0 18px 32px -16px rgba(50, 85, 164, .5)`): hover on the Give door, with a 3px rise.

### Named Rules

**The Lift Is a Response Rule.** Surfaces lie flat at rest. Only a hover from a pointer that can hover lifts a button or the Give door, and the shadow is always blue-tinted, never grey or black.

## Shapes

Everything is square (0 radius): doors, boxes, buttons, the dock, focus rings. Lines are 3px blue strokes: section rules, the header and dock rules, the top rule over each step, outline button borders. One dashed 3px rule exists, and it means urgent outside help. Icons are inline SVG line drawings at 1.1em, 2.2 stroke, round caps and joins, in `currentColor`. The logo is an SVG in `currentColor`, so CSS sets its ink; its two wings are separate groups so they can spread.

**The Dashed Means Urgent Rule.** A dashed rule is reserved for time-critical help that someone else provides (the hotline note). Do not use it for decoration, placeholders or emphasis.

## Components

### Buttons
Solid, square, confident blocks of ink with a bold sentence-case label and an optional line icon.
- **Shape:** square (0px), 3px border in the fill's own ink, min-height 48px (44px for the small size).
- **Outline (default):** transparent fill, blue border and label. Used for secondary actions such as Copy address.
- **Blue:** blue fill, paper label. The primary action on paper and on sunflower (Email us in the steps, Donate on Chuffed in the Give box, Get help in the dock).
- **Sunflower:** sunflower fill and border, overprint label. Donate in the header, the dock and the 404 page.
- **Paper:** paper fill, blue label. Used only inside the blue Need-help door.
- **On sunflower:** an outline button inside the Give box draws its border and label in overprint (Share the fund).
- **Hover (hover-capable pointers only):** rises 2px with the button-lift shadow; a trailing arrow slides 5px right. 0.18s on the house ease.
- **Active:** returns to baseline with the tighter press shadow, 0.08s.
- **Focus:** 3px solid blue outline at 4px offset; sunflower inside blue containers.
- **Done:** Copy and Share confirm by turning sunflower with an overprint "Copied" or "Link copied" and a check icon for 2 seconds, announced through a polite live region. Both buttons exist only when JavaScript runs.

### The two doors (signature)
The first screen offers two doors, one per audience.
- **Give door:** a sunflower plate with a blue door headline, overprint copy, and an overprint underlined "Donate on Chuffed" link with an arrow. The whole door follows that one link. Hover lifts it 3px with the door-lift shadow and slides the arrow 6px.
- **Need-help door:** a blue block with a paper headline and copy, a paper "Email us" button, a bold paper text link to the help section, and the plain email address in small type. It does not lift: it holds two actions.
- **Shape:** square, padding clamp(24px, 3vw, 36px), copy at 32ch.

### Header and nav
- **Style:** sticky, paper, 68px, 3px blue bottom rule. Logo mark at 34px tall links to the top. Nav links bold 0.95rem, 26px apart, then a small sunflower Donate button.
- **Current section:** a sunflower ink band (8px tall, multiply) slides and stretches under the link for the section in view (0.45s), and the link takes `aria-current="location"` with a 2px underline. Nothing is marked while the hero is in view.
- **Hover:** links underline. **Phones:** nav and Donate hide; the dock replaces them.

### Steps list
Three numbered steps for getting help, as an ordered list.
- Each step sits under its own 3px blue rule. The numeral is blue League Gothic at 6rem with a sunflower band (inset 14% 0 8%) printed over it with multiply, so the numeral reads in overprint.
- Title in League Gothic caps at 2.3rem; copy at 36ch. Step one carries the blue Email us button, the outline Copy address button and the plain address.
- On hover-capable pointers with motion allowed, hovering a step nudges its band (3px, -2px) out of register.

### Urgent note
- A dashed 3px blue frame, padding 20px 24px, wrapping flex row: a 1.9rem League Gothic title beside a 50ch paragraph. The phone number is a bold `tel:` link that never wraps. It names who runs the service.

### Where we fit
- A two-column block under a 3px rule: League Gothic title left (min 12ch), up to four paragraphs right at 52ch with underlined links to the organizations it names. One column on phones.

### Give box
- A sunflower block (padding clamp(24px, 3vw, 40px)) with an overprint "Kickoff goal" label, the goal figure in blue League Gothic, then a blue Donate on Chuffed button and the overprint Share the fund button. Beside it, three facts in a check-icon list at 52ch.

### Footer
- 3px blue top rule, 40px top padding and 120px bottom padding so the last links clear the phone dock. Three columns: the logo mark (44px) with the organization line and small print; Contact; and the organizations the fund stands alongside. Column titles in League Gothic at 1.6rem. Links are underlined blue text.

### Phone dock
- Phones only (53.75em and below). Fixed to the bottom, paper, 3px blue top rule, padding 12px 16px plus the safe-area inset. Two equal buttons: blue "Get help" with a down arrow (to the help section) and sunflower "Donate" (to Chuffed).
- It shows whenever the Need-help door's buttons are out of view, so on a phone it is there from the first screen. It steps aside, sliding down in 0.28s and becoming hidden to assistive tech and focus, while those door buttons are visible and once the footer is in view.

### Links, focus and selection
- Links inherit their ink, underlined 2px at a 0.2em offset; hover thickens the underline to 3px. On blue, links are bold paper.
- Focus: 3px solid outline at 4px offset, blue on paper and sunflower, sunflower inside blue containers. A blue skip link slides in from above on focus.
- Text selection prints sunflower with overprint text.

### The print run (signature motion)
The page prints itself once on load, on one ease, cubic-bezier(.16, 1, .3, 1).
- **Blue plate:** the logo, each headline line, the lede and both doors start 7px left and 4px low and settle into registration over 0.75s. Headline lines stagger by 70ms; the lede follows at 280ms, the help door at 200ms.
- **Sunflower plate:** the "Boston’s" band and the Give door's ink start from the opposite side (16px right, 10px up) and land over 0.9s, 160ms after their blue.
- **Wings:** each wing spreads outward from the body (scaleX 0.08 to 1, fading in over the first 35%) in 1.1s after 120ms.
- **Ink over the steps:** when the steps list first scrolls into view, sunflower wipes left to right over each numeral in turn (0.5s each, starting 100ms, 260ms and 420ms). It runs once.
- Entrance animations use `animation-fill-mode: backwards`, so they hold their start position during the delay and release every transform when they finish; hover lifts are never pinned.

**The Registration Rule.** Motion moves plates, never meaning. Every word is readable at every instant: content is only offset by a few pixels, and only ink (the wings, the bands) is ever undrawn.

### Reduced motion, forced colors, no script, print
- **Reduced motion:** no print run; every band is drawn from the start; hover lifts and arrow slides are removed; the nav ink and dock change in 0.01s; smooth scrolling is off.
- **Forced colors:** the nav band stops blending, and the "Boston’s" and numeral bands are removed, because the system would paint them opaque over the letters. Everything else falls to system colours.
- **No JavaScript:** the page reads and works fully. Copy and Share buttons are not shown, the step bands are drawn from the start, the nav ink and the dock stay hidden, and every link goes where it says.
- **Print:** header, dock and script-only controls are hidden on a white page.

## Do's and Don'ts

### Do:
- **Do** print with blue (#3255A4) and sunflower (#FFB511) on paper (#FBFAF6) only, and let overprint (#2E3A10) appear where they cross.
- **Do** set every small text on sunflower in overprint; keep blue on sunflower for display type at 41.6px and up.
- **Do** print highlight bands over the letters with `mix-blend-mode: multiply` inside an isolated stacking context, so the crossed letters turn overprint.
- **Do** open every section with a full-width 3px blue rule and clamp(56px, 8vw, 112px) of block padding.
- **Do** keep every block, button and box square, filled with solid ink.
- **Do** put every hover effect inside `@media (hover: hover)` and every authored motion inside `prefers-reduced-motion: no-preference`.
- **Do** give entrance animations `animation-fill-mode: backwards`.
- **Do** keep the give door and the get-help door reachable from the first screen at every width: hero doors on wide screens, the dock on phones.
- **Do** keep buttons at least 44px tall (48px at the default size) and write breakpoints in em.

### Don't:
- **Don't** add a third colour, tints, visible gradients or grey shadows; the only translucent blue is the hover and press shadow.
- **Don't** put blue or paper small text on sunflower, or any text in sunflower on paper.
- **Don't** set sentences, labels or buttons in League Gothic, or headings in Atkinson Hyperlegible.
- **Don't** set any type larger than 6rem.
- **Don't** round corners or float cards on shadows at rest.
- **Don't** use a dashed rule for anything except urgent help someone else provides.
- **Don't** fade, blur or hold back words in motion; only ink may be undrawn.
- **Don't** add photographs, stock or enforcement imagery, stat counters, rows of identical icon cards, or labels stacked above headings.
- **Don't** load fonts, images or scripts from another host, or embed the donation platform in a frame.

## Accessibility

The site targets WCAG 2.2 AA and is built for someone reading under stress, on a phone, over a weak connection, possibly in a second language.

- **Contrast:** every text pair is listed under Colors. Text on paper or blue is at least 6.5:1; small text on sunflower is 6.6:1 or better; the 4.0:1 pair is display-only.
- **Reading size:** body text is 18px Atkinson Hyperlegible at 1.55 line height, measures capped between 32 and 70ch.
- **Targets:** buttons are at least 44px tall; the dock buttons split the screen width.
- **Focus:** always visible (3px, 4px offset), coloured for its background; a skip link leads the page; the main region takes focus without an outline.
- **Structure:** one `h1`; sections labelled by their headings; the steps are an ordered list whose decorative numerals are hidden from assistive tech; the dock is a labelled navigation region; copy and share results are announced in a polite live region.
- **Motion and colour modes:** full reduced-motion and forced-colors paths, described under Components.
- **Resilience:** works with JavaScript off; breakpoints in em so larger default text gets the phone layout; landscape phones get their screen back; no horizontal scroll at 320px.
- **Privacy:** no cookies, analytics, third-party requests or forms. Fonts are self-hosted and a Content-Security-Policy limits every resource to the site itself. The help path warns that email isn't fully private.

## Content

The design depends on the copy staying plain, factual and confirmed.

- **Source:** public copy follows the organization's own drafts: its tag, short description and medium description. The hero lede is the short description; "Where we fit" is the medium description.
- **No invented claims:** no testimonials, stories, counts of people helped, impact figures, team bios, client photos, endorsements, live progress or claims about how much of each gift reaches the fund. Tax language stays "to the extent allowed by law".
- **"May" where eligibility is unconfirmed:** the help door says the fund "may be able to help", and the third step reads "We may help with legal fees". Firm promises about who qualifies or what is covered wait until they are confirmed.
- **Partners named accurately:** other organizations are named as groups the fund "stands alongside", with their services described in their own terms and a clear line on who runs what ("run by LUCE, not by us").
- **Names:** Boston Angel Network Inc. is the 501(c)(3); the Boston Angel Fund is its legal-fee fund.
- **Typography in copy:** curly apostrophes and quotes, en dashes for ranges, and no-break spans for 501(c)(3), the EIN, phone numbers and short place names.

## Maintenance

- **Where things live:** all copy is in `site/index.html`; tokens are the custom properties at the top of `site/css/site.css` (`--blue`, `--sun`, `--over`, `--paper`, `--gutter`, `--ease`, `--rule`); behaviour is in `site/js/site.js`. There is no build step.
- **The goal figure:** the $1,000 goal appears twice on the page, in the Give door's sentence and in the Give box figure. Change both together. The share image (`site/assets/og-image.png`, rendered from `tools/og/og.html`) does not print the figure today; if it ever does, it becomes a third place to change.
- **The share image:** `tools/og/og.html` repeats the headline, the inks and the type at 1200 × 630. Re-render it whenever the headline or the inks change (the command is in `README.md`).
- **Fonts:** the WOFF2 files are Latin subsets. After adding copy with new characters (another language, new symbols), run the checks in `tools/fonts/` and rebuild if any character is missing, or it will fall back to a system face.
- **Security policy:** the page's Content-Security-Policy allows only same-origin scripts, styles, fonts and images. Keep styles in `site.css` and scripts in `site.js`; inline `<style>`, `style=""` attributes and inline scripts are blocked.
- **Deploy:** every push to `main` runs a GitHub Actions workflow that copies `site/`, runs `tools/deploy/prepare.py`, and publishes the result to GitHub Pages. The script makes the share image URL absolute, adds `og:url`, a canonical link and the JSON-LD `url` for the live address, prefixes the 404 page's root paths (`/css/site.css`) with the Pages base path, and drops `_headers`, which Pages ignores. It matches the exact tag `<meta property="og:image" content="assets/og-image.png">`, so keep that line as written, and keep the 404 page's links root-relative.
