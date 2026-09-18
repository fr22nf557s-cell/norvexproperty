# Norvex Property

norvexproperty.com. A scroll-driven film of the flagship listing, six service
pages, valuation and contact forms, insights, and a full legal suite.

## How the site is built

Every page is rendered from one layout by `tools/build.py`, so the header,
menus, footer, metadata, structured data and sitemap never drift between
pages.

    python3 tools/build.py --check

`--check` verifies internal links, fragments, duplicate ids, headings and copy
rules after building. Page content lives in `tools/pages/`; company details
(email, phone, company number, registered office, redress and client money
schemes) live in `tools/site.json` and flow into the footer and legal pages.

## The mark

The N in the lozenge is not a lookalike: `tools/logo.py` lifts the outline
straight out of the Cormorant Garamond file the site already serves, so the
mark and the wordmark are the same cut of type. It writes every SVG the site
uses, including `tools/mark.svg`, the fragment the page builder inlines into
the header, the footer, the menu and the printed letterhead, coloured by the
stylesheet rather than by hardcoded fills.

    python3 tools/logo.py           # redraw the SVGs (needs fonttools)
    node tools/rasterise.mjs        # render the PNG icons (needs Playwright)
    python3 tools/logo.py --ico     # pack favicon.ico at 16, 32 and 48
    python3 tools/logo.py --check   # fail if a committed SVG is out of date

There are two weights of one drawing: the line mark everywhere above 20px, and
a filled lozenge with the N knocked out for the browser tab, where a hairline
would disappear.

## Photography and the film

Everything visual comes from one 4K master of the film. `tools/media.py` cuts
each still into an AVIF and WebP ladder, records what it produced in
`assets/img/manifest.json`, and `tools/img.py` turns that into `<picture>`
markup, so a page can only reference a file that exists and `--check` fails if
one goes missing. Masters live in `assets/master/` and are not committed.

The film ships at four sizes plus a 9:16 cut for phones held upright, and
`assets/home.js` picks between them by viewport, pixel density, orientation and
the visitor's data preference. Rebuild any of it with the "Build media"
workflow in the Actions tab, which takes the master's URL and can do the images
and the film independently.

Generated pages are committed, and GitHub Pages serves the `main` branch at
the domain set in `CNAME`. Fonts, photography and the film are served from
this repository; the site sets no cookies and loads nothing from third
parties when browsed. Forms are relayed by FormSubmit to the configured email
address, with a mail-app fallback.
