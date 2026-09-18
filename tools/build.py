#!/usr/bin/env python3
"""Build the Norvex Property site: every page rendered from one layout.

    python3 tools/build.py          # writes pages into the repository root
    python3 tools/build.py --check  # build, then verify links, ids and assets

Page modules live in tools/pages/. Each exposes PAGES, a list of dicts.
"""
import html, importlib, json, os, re, sys, datetime, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from img import picture, CARD_SIZES, FULL_SIZES, HERO_SIZES, STAGE_SIZES  # noqa: E402
SITE = json.loads((ROOT / "tools" / "site.json").read_text())
TODAY = datetime.date.today().isoformat()

SERVICES = [
    ("/services/buy/", "Buy", "Search, viewings, offers and the path to completion."),
    ("/services/sell/", "Sell", "Valuation, presentation, marketing and negotiation."),
    ("/services/let/", "Let", "Lettings and management for landlords and tenants."),
    ("/services/mortgages/", "Mortgages", "Whole-of-market advice and a decision in principle in days."),
    ("/services/bridging/", "Bridging finance", "Short-term secured lending from £150,000."),
    ("/services/surveying/", "Surveying", "RICS Level 2 and Level 3 surveys and defect reports."),
]
COMPANY = [("/about/", "About"), ("/valuation/", "Book a valuation"), ("/insights/", "Insights"), ("/careers/", "Careers"), ("/contact/", "Contact"), ("/legal/complaints/", "Complaints")]
LEGAL = [("/legal/terms/", "Terms and conditions"), ("/legal/privacy/", "Privacy notice"), ("/legal/cookies/", "Cookies"), ("/legal/fees/", "Fees and client money"), ("/legal/accessibility/", "Accessibility"), ("/legal/aml/", "Identity and anti-money laundering checks")]

def e(s):
    return html.escape(str(s), quote=True)

def jsonld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/") + "</script>"

def org():
    o = {"@type": "RealEstateAgent", "@id": SITE["domain"] + "/#org", "name": SITE["name"], "legalName": SITE["legal_name"], "url": SITE["domain"] + "/",
         "logo": SITE["domain"] + "/icon-512.png", "image": SITE["domain"] + "/assets/img/manor-poster.jpg", "email": SITE["email"],
         "description": "Estate agency for sales, lettings, mortgages, bridging finance and RICS surveys.",
         "areaServed": ["London", "Cotswolds", "Surrey", "Somerset", "Buckinghamshire"], "address": {"@type": "PostalAddress", "addressLocality": "London", "addressCountry": "GB"}}
    if SITE.get("phone"): o["telephone"] = SITE["phone"]
    same = [v for v in SITE.get("social", {}).values() if v]
    if same: o["sameAs"] = same
    return o

def head(p):
    url = SITE["domain"] + p["path"]
    og = SITE["domain"] + p.get("og_image", "/assets/img/manor-poster.jpg")
    title = p["title"] if p.get("title_raw") else (p["title"] + " | " + SITE["name"] if p["path"] != "/" else SITE["name"] + " | Buy, let, sell, finance and survey")
    robots = "noindex, nofollow" if p.get("noindex") else "index, follow, max-image-preview:large"
    parts = [
        '<meta charset="utf-8">', '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">',
        f"<title>{e(title)}</title>", f'<meta name="description" content="{e(p["description"])}">',
        f'<link rel="canonical" href="{e(url)}">', f'<meta name="robots" content="{robots}">', '<meta name="theme-color" content="#0B0C10">',
        '<meta property="og:type" content="website">', f'<meta property="og:site_name" content="{e(SITE["name"])}">', '<meta property="og:locale" content="en_GB">',
        f'<meta property="og:url" content="{e(url)}">', f'<meta property="og:title" content="{e(title)}">', f'<meta property="og:description" content="{e(p["description"])}">',
        f'<meta property="og:image" content="{e(og)}">', '<meta property="og:image:width" content="1920">', '<meta property="og:image:height" content="1080">',
        '<meta name="twitter:card" content="summary_large_image">', f'<meta name="twitter:title" content="{e(title)}">', f'<meta name="twitter:description" content="{e(p["description"])}">', f'<meta name="twitter:image" content="{e(og)}">',
        '<link rel="icon" href="/favicon.svg" type="image/svg+xml">', '<link rel="icon" href="/favicon.ico" sizes="32x32">', '<link rel="apple-touch-icon" href="/apple-touch-icon.png">', '<link rel="manifest" href="/site.webmanifest">',
        '<link rel="preload" href="/assets/fonts/cormorant-garamond.woff2" as="font" type="font/woff2" crossorigin>', '<link rel="preload" href="/assets/fonts/montserrat.woff2" as="font" type="font/woff2" crossorigin>',
        '<link rel="stylesheet" href="/assets/fonts.css">', '<link rel="stylesheet" href="/assets/site.css">',
    ]
    if p.get("css"): parts.append("<style>" + p["css"] + "</style>")
    ld = [org()] if p["path"] == "/" else []
    if p["path"] == "/":
        ld.append({"@type": "WebSite", "@id": SITE["domain"] + "/#website", "name": SITE["name"], "url": SITE["domain"] + "/", "publisher": {"@id": SITE["domain"] + "/#org"}})
    if p.get("crumbs"):
        ld.append({"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": SITE["domain"] + h} for i, (h, n) in enumerate([("/", "Home")] + p["crumbs"])]})
    ld += p.get("jsonld", [])
    parts.append(jsonld({"@context": "https://schema.org", "@graph": ld}))
    return "\n".join(parts)

def cur_attr(href, current):
    return ' aria-current="page"' if href == current else ""

def nav_item(href, label, current):
    cur = ' aria-current="page"' if href == current else ""
    return f'<li><a href="{href}"{cur}>{e(label)}</a></li>'

def header(p):
    cur = p["path"]
    services_open = any(cur == h for h, _, _ in SERVICES)
    svc = "".join(f'<li><a href="{h}"{cur_attr(h, cur)}>{e(n)}<small>{e(d)}</small></a></li>' for h, n, d in SERVICES)
    solid = "" if p.get("home") else " hdr--solid"
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="hdr{solid}">
  <div class="hdr__in">
    <a class="brand" href="/"><i aria-hidden="true"></i>{e(SITE["name"])}</a>
    <nav aria-label="Primary"><ul class="nav">
      <li data-menu data-open="false"><button class="nav__btn" type="button" aria-expanded="false" aria-haspopup="true"{cur_attr(True, services_open)}>Services</button><ul class="nav__panel">{svc}</ul></li>
      {nav_item("/valuation/", "Valuation", cur)}{nav_item("/insights/", "Insights", cur)}{nav_item("/about/", "About", cur)}{nav_item("/contact/", "Contact", cur)}
    </ul></nav>
    <div class="hdr__right">
      <a class="cta-enquire-nav" href="/valuation/">Book a valuation</a>
      <button class="menu-btn" id="menu-btn" type="button" aria-expanded="false" aria-controls="menu">Menu</button>
    </div>
  </div>
</header>
<div class="menu" id="menu" hidden>
  <button class="menu__close" id="menu-close" type="button">Close</button>
  <p class="menu__label">Services</p>
  <ul class="menu__group">{"".join(f'<li><a href="{h}">{e(n)}<small>{e(d)}</small></a></li>' for h, n, d in SERVICES)}</ul>
  <p class="menu__label">Company</p>
  <ul class="menu__group">{"".join(f'<li><a href="{h}">{e(n)}</a></li>' for h, n in COMPANY)}</ul>
  <p class="menu__label">Legal</p>
  <ul class="menu__group">{"".join(f'<li><a href="{h}">{e(n)}</a></li>' for h, n in LEGAL)}</ul>
</div>'''

def footer():
    lines = []
    lines.append(f'{e(SITE["name"])} is the trading name of {e(SITE["legal_name"])}, a company registered in England and Wales.')
    if SITE.get("company_number"): lines.append(f'Company number {e(SITE["company_number"])}.')
    if SITE.get("registered_office"): lines.append(f'Registered office: {e(SITE["registered_office"])}.')
    if SITE.get("vat_number"): lines.append(f'VAT registration {e(SITE["vat_number"])}.')
    if SITE.get("ico_number"): lines.append(f'ICO registration {e(SITE["ico_number"])}.')
    if SITE.get("redress_scheme"): lines.append(f'Member of {e(SITE["redress_scheme"])}.')
    if SITE.get("cmp_scheme"): lines.append(f'Client money protection: {e(SITE["cmp_scheme"])}.')
    lines.append(SITE.get("fca_statement") or "Mortgage and bridging advice is provided by our FCA-authorised partners; Norvex Property introduces clients and does not itself give regulated financial advice.")
    lines.append("Your home may be repossessed if you do not keep up repayments on a mortgage or any other debt secured on it. Bridging loans are secured on property and carry higher interest than a standard mortgage. Figures shown on this website are indicative, not offers.")
    contact = f'<a href="mailto:{e(SITE["email"])}">{e(SITE["email"])}</a>'
    if SITE.get("phone"): contact += f' · <a href="{e(SITE["phone_href"] or "tel:" + SITE["phone"])}">{e(SITE["phone"])}</a>'
    return f'''<footer class="ftr">
  <div class="wrap">
    <div class="ftr__grid">
      <div>
        <p class="brand" style="margin:0">{e(SITE["name"])}</p>
        <p class="ftr__tag">Buy. Let. Sell. Finance. Survey.</p>
        <p class="ftr__blurb">Four practices under one roof: sales and lettings, mortgages, bridging finance and surveying. One quiet, exact team from first viewing to completion.</p>
        <p class="ftr__blurb">{contact}<br>{e(SITE["opening_hours"])}</p>
      </div>
      <div><h2>Services</h2><ul>{"".join(f'<li><a href="{h}">{e(n)}</a></li>' for h, n, _ in SERVICES)}</ul></div>
      <div><h2>Company</h2><ul>{"".join(f'<li><a href="{h}">{e(n)}</a></li>' for h, n in COMPANY)}</ul></div>
      <div><h2>Legal</h2><ul>{"".join(f'<li><a href="{h}">{e(n)}</a></li>' for h, n in LEGAL)}</ul></div>
    </div>
    <div class="ftr__bottom">
      <p class="ftr__legal">{" ".join(lines)}</p>
      <div class="ftr__meta"><span>&copy; <span data-year>{datetime.date.today().year}</span> {e(SITE["legal_name"])}. All rights reserved.</span><a href="/legal/privacy/">Privacy</a><a href="/legal/cookies/">Cookies</a><a href="/legal/accessibility/">Accessibility</a><a href="/sitemap.xml">Sitemap</a></div>
    </div>
  </div>
</footer>'''


def hero(p):
    h = p.get("hero")
    if not h: return ""
    crumbs = ""
    if p.get("crumbs"):
        items = '<li><a href="/">Home</a></li>' + "".join(f'<li><a href="{href}">{e(n)}</a></li>' if href != p["path"] else f'<li><span aria-current="page">{e(n)}</span></li>' for href, n in p["crumbs"])
        crumbs = f'<nav aria-label="Breadcrumb"><ol class="crumbs">{items}</ol></nav>'
    img = h.get("image", "/assets/img/still-aerial.jpg")
    pos = h.get("pos", "50% 50%")
    short = " phero--short" if h.get("short") else ""
    lead = f'<p class="lead">{h["lead"]}</p>' if h.get("lead") else ""
    actions = f'<div class="band__actions" style="margin-top:28px">{h["actions"]}</div>' if h.get("actions") else ""
    return f'''<section class="phero{short}" style="--pos:{pos}">
  {picture(img, HERO_SIZES, cls="phero__img", pic_cls="phero__pic", eager=True)}
  <div class="phero__in">{crumbs}<p class="eyebrow">{e(h["eyebrow"])}</p><h1 class="h1">{h["h1"]}</h1>{lead}{actions}</div>
</section>'''

def render(p):
    scripts = '<script src="/assets/site.js" defer></script>' + ('<script src="/assets/home.js" defer></script>' if p.get("home") else "") + p.get("scripts", "")
    body_class = ' class="is-home"' if p.get("home") else ""
    return f'''<!DOCTYPE html>
<html lang="en-GB">
<head>
{head(p)}
</head>
<body{body_class} data-email="{e(SITE["email"])}">
{header(p)}
<main id="main" tabindex="-1">
{hero(p)}
{p["body"]}
</main>
{footer()}
{scripts}
</body>
</html>
'''

def load_pages():
    pages = []
    pkg = ROOT / "tools" / "pages"
    sys.path.insert(0, str(ROOT / "tools"))
    for f in sorted(pkg.glob("*.py")):
        if f.name.startswith("_"): continue
        mod = importlib.import_module("pages." + f.stem)
        pages += mod.PAGES
    seen = set()
    for p in pages:
        assert p["path"] not in seen, "duplicate path " + p["path"]; seen.add(p["path"])
        assert p["path"].startswith("/") and (p["path"].endswith("/") or p["path"].endswith(".html")), p["path"]
    return pages

def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

def build():
    pages = load_pages()
    out = []
    for p in pages:
        target = ROOT / (p["path"].lstrip("/") + ("index.html" if p["path"].endswith("/") else ""))
        write(target, render(p)); out.append(target)
    urls = [p for p in pages if not p.get("noindex")]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for p in urls:
        sm.append(f'  <url><loc>{e(SITE["domain"] + p["path"])}</loc><lastmod>{p.get("modified", TODAY)}</lastmod><changefreq>{p.get("changefreq", "monthly")}</changefreq><priority>{p.get("priority", "0.6")}</priority></url>')
    sm.append("</urlset>")
    write(ROOT / "sitemap.xml", "\n".join(sm) + "\n")
    write(ROOT / "robots.txt", f"User-agent: *\nAllow: /\nDisallow: /tools/\n\nSitemap: {SITE['domain']}/sitemap.xml\n")
    exp = (datetime.date.today() + datetime.timedelta(days=364)).isoformat()
    write(ROOT / ".well-known" / "security.txt", f"Contact: mailto:{SITE['email']}\nExpires: {exp}T00:00:00.000Z\nPreferred-Languages: en\nCanonical: {SITE['domain']}/.well-known/security.txt\n")
    (ROOT / ".nojekyll").write_text("")
    print(f"built {len(out)} pages")
    return pages

def check(pages):
    """Verify every internal link, fragment and asset resolves."""
    problems = []
    ids = {}
    docs = {}
    for p in pages:
        f = ROOT / (p["path"].lstrip("/") + ("index.html" if p["path"].endswith("/") else ""))
        t = f.read_text(encoding="utf-8"); docs[p["path"]] = t
        ids[p["path"]] = set(re.findall(r'\sid="([^"]+)"', t))
        dup = [i for i in re.findall(r'\sid="([^"]+)"', t) if re.findall(r'\sid="%s"' % re.escape(i), t).__len__() > 1]
        if dup: problems.append(f'{p["path"]}: duplicate ids {sorted(set(dup))}')
        if "—" in t or "–" in re.sub(r"<script[\s\S]*?</script>", "", t): problems.append(f'{p["path"]}: dash character in copy')
        if re.search(r"lorem|TODO|placeholder|\[to be", t, re.I): problems.append(f'{p["path"]}: placeholder text')
        if t.count("<h1") != 1: problems.append(f'{p["path"]}: {t.count("<h1")} h1 elements')
    for path, t in docs.items():
        for m in re.finditer(r'(?:href|src)="([^"]+)"', t):
            u = m.group(1)
            if u.startswith(("http", "mailto:", "tel:", "data:", "#")):
                if u.startswith("#") and u != "#" and u[1:] not in ids[path]: problems.append(f"{path}: missing fragment {u}")
                continue
            base, _, frag = u.partition("#")
            base = base.split("?")[0]
            if base.endswith("/"): target = ROOT / (base.lstrip("/") + "index.html")
            else: target = ROOT / base.lstrip("/")
            if not target.exists(): problems.append(f"{path}: broken link {u}")
            elif frag:
                tp = base if base.endswith("/") else None
                if tp and tp in ids and frag not in ids[tp]: problems.append(f"{path}: missing fragment {u}")
    for path in ("/404.html",):
        pass
    if problems:
        print("\n".join(problems)); sys.exit(1)
    print(f"checked {len(docs)} pages: links, fragments, ids, copy OK")

if __name__ == "__main__":
    pages = build()
    if "--check" in sys.argv: check(pages)
