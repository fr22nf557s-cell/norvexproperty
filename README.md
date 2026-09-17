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

Generated pages are committed, and GitHub Pages serves the `main` branch at
the domain set in `CNAME`. Fonts, photography and the film are served from
this repository; the site sets no cookies and loads nothing from third
parties when browsed. Forms are relayed by FormSubmit to the configured email
address, with a mail-app fallback.
