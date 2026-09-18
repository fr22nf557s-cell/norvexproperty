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
