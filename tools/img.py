"""Responsive <picture> markup backed by the ladder tools/media.py builds.

Both the layout and the page modules use this, so it lives on its own to keep
the imports one-way.
"""
import html, json, os, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
MANIFEST_PATH = ROOT / "assets" / "img" / "manifest.json"
MANIFEST = json.loads(MANIFEST_PATH.read_text()) if MANIFEST_PATH.exists() else {}

# What a card image actually occupies: full width on a phone, a column of the
# three-up grid above that. Telling the browser this is what stops it pulling a
# hero-sized file for a thumbnail, and what makes it pull a 2x one on retina.
CARD_SIZES = "(max-width:700px) 92vw, (max-width:1100px) 46vw, 400px"
FULL_SIZES = "100vw"
# A cover-fitted 16:9 image in a box that is taller than 9/16 of its width is
# scaled up until it covers, so the pixels it really needs are set by the box
# height, not its width. These say so: 110vh is a 62vh-tall hero, 178vh a
# full-screen one. Getting this wrong is what leaves a hero soft on a phone.
HERO_SIZES = "max(100vw, 110vh)"
STAGE_SIZES = "max(100vw, 178vh)"
# Phones with a 3x screen would otherwise ask for the 4K step and spend a
# megabyte to beat a 2560 file no one can tell apart at arm's length.
NARROW_CAP = 2560
NARROW_MEDIA = "(max-width:700px)"
# The film stage fills the screen, so a phone held upright crops a landscape
# frame to a sliver. This asks for the 9:16 cut instead.
UPRIGHT_MEDIA = "(orientation:portrait) and (max-width:900px)"


def srcset(name, fmt, widths):
    return ", ".join(f"/assets/img/{name}-{w}.{fmt} {w}w" for w in widths)


def picture(src, sizes=FULL_SIZES, alt="", cls="", pic_cls="", eager=False, extra="", art=()):
    """An <img> wrapped in its AVIF and WebP ladder.

    Falls back to the plain <img> when the ladder has not been generated yet,
    so the site always builds from a clean checkout.
    """
    name = os.path.basename(src).rsplit(".", 1)[0]
    entry = MANIFEST.get(name)
    load = ' fetchpriority="high"' if eager else ' loading="lazy"'
    klass = f' class="{cls}"' if cls else ""
    alt_attr = html.escape(str(alt), quote=True)
    img = (f'<img{klass} src="{src}" alt="{alt_attr}" width="1920" height="1080"'
           f'{load} decoding="async"{extra}>')
    if not entry:
        return img
    sources = ""
    # Art direction first: a differently cropped master for a screen shape the
    # main image would have to crop hard to fill.
    for media, alt_name, alt_sizes in art:
        alt_entry = MANIFEST.get(alt_name)
        if not alt_entry:
            continue
        for fmt, mime in (("avif", "image/avif"), ("webp", "image/webp")):
            widths = alt_entry.get(fmt) or []
            if widths:
                sources += (f'<source type="{mime}" media="{media}" '
                            f'srcset="{srcset(alt_name, fmt, widths)}" sizes="{alt_sizes}">')
    for fmt, mime in (("avif", "image/avif"), ("webp", "image/webp")):
        widths = entry.get(fmt) or []
        if not widths:
            continue
        capped = [w for w in widths if w <= NARROW_CAP]
        if capped and capped != widths:
            sources += (f'<source type="{mime}" media="{NARROW_MEDIA}" '
                        f'srcset="{srcset(name, fmt, capped)}" sizes="{sizes}">')
        sources += f'<source type="{mime}" srcset="{srcset(name, fmt, widths)}" sizes="{sizes}">'
    pk = f' class="{pic_cls}"' if pic_cls else ""
    return f"<picture{pk}>{sources}{img}</picture>"
