#!/usr/bin/env python3
"""Draw the Norvex Property mark.

The mark is the brand's own letter: the N is taken from the Cormorant Garamond
file the site already serves, so the mark and the wordmark are cut from exactly
the same typeface rather than merely resembling each other. It sits in the
lozenge the site has always used, which keeps the identity continuous.

Two weights of the same drawing:
  line   the mark proper, for the header, the footer and anything above 20px
  solid  a filled lozenge with the N knocked out, which survives a 16px tab

    python3 tools/logo.py            # write the SVGs
    python3 tools/logo.py --check    # verify the committed SVGs are current

Requires fonttools. The PNG and ICO icons are rendered from these SVGs by
tools/rasterise.mjs, which needs node and Playwright.
"""
import argparse
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
FONT = ROOT / "assets" / "fonts" / "cormorant-garamond.woff2"

INK = "#0B0C10"
IVORY = "#F3EEE4"
CHAMPAGNE = "#E9D6AE"


def glyph_path(weight):
    """The outline of N at a given weight, with its bounding box."""
    from fontTools.ttLib import TTFont
    from fontTools.varLib.instancer import instantiateVariableFont
    from fontTools.pens.svgPathPen import SVGPathPen
    from fontTools.pens.boundsPen import BoundsPen

    font = instantiateVariableFont(TTFont(FONT), {"wght": weight}, inplace=True,
                                   updateFontNames=False)
    glyphs = font.getGlyphSet()
    name = font.getBestCmap()[ord("N")]
    pen, bounds = SVGPathPen(glyphs), BoundsPen(glyphs)
    glyphs[name].draw(pen)
    glyphs[name].draw(bounds)
    return pen.getCommands(), bounds.bounds


def n(weight, cap, fill, cx=32.0, cy=32.0, cls=""):
    """The N scaled to a cap height and centred on (cx, cy) in a 64 box."""
    d, (x0, y0, x1, y1) = glyph_path(weight)
    s = cap / (y1 - y0)
    tx = cx - (x1 - x0) * s / 2 - x0 * s
    ty = cy + cap / 2 + y0 * s  # glyph space is y-up, so the scale flips
    k = f' class="{cls}"' if cls else ""
    return (f'<g{k} transform="translate({tx:.3f} {ty:.3f}) scale({s:.5f} {-s:.5f})">'
            f'<path d="{d}" fill="{fill}"/></g>')


def lozenge(r, stroke, width, cls=""):
    a, b = round(32 - r, 2), round(32 + r, 2)
    k = f' class="{cls}"' if cls else ""
    return (f'<path{k} d="M32 {a} {b} 32 32 {b} {a} 32Z" fill="none" '
            f'stroke="{stroke}" stroke-width="{width}" stroke-linejoin="miter"/>')


def line_mark(rule=CHAMPAGNE, letter=IVORY, width=2.6):
    # The rule sits a whisker clear of the N's serifs: any tighter and they
    # touch at small sizes, any looser and the lozenge reads as empty.
    return lozenge(25.5, rule, width) + n(600, 23, letter)


def solid_mark(field=CHAMPAGNE, letter=INK):
    # Heavier and larger than the line mark: at a 16px tab the N has to survive
    # as a shape, not as a drawing.
    return (f'<path d="M32 3.5 60.5 32 32 60.5 3.5 32Z" fill="{field}"/>'
            + n(700, 26, letter))


def svg(body, title, plate=None, pad=0):
    """Wrap a 64-unit drawing, optionally on a rounded plate with padding."""
    inner = body
    if pad:
        k = (64 - 2 * pad) / 64
        inner = f'<g transform="translate({pad} {pad}) scale({k:.5f})">{body}</g>'
    back = f'<rect width="64" height="64" rx="{12 if plate == "round" else 0}" fill="{INK}"/>' if plate else ""
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" role="img" '
            f'aria-label="{title}">{back}{inner}</svg>\n')


def files():
    """Every SVG the site keeps on disk, by path."""
    return {
        # the tab icon: solid, on a plate, because tabs are 16px and often light
        "favicon.svg": svg(solid_mark(), "Norvex Property", plate="round", pad=5),
        # the full mark, for app icons, press and anywhere it stands alone
        "assets/logo.svg": svg(line_mark(), "Norvex Property"),
        "assets/logo-solid.svg": svg(solid_mark(), "Norvex Property"),
        # icon sources: plate behind, and the maskable one keeps clear of the crop
        "assets/icon-source.svg": svg(line_mark(width=2.2), "Norvex Property", plate="round", pad=7),
        "assets/icon-maskable-source.svg": svg(line_mark(width=2.6), "Norvex Property", plate="square", pad=13),
        # iOS applies its own corner radius, so this one is square to the edge
        "assets/apple-source.svg": svg(line_mark(width=2.4), "Norvex Property", plate="square", pad=9),
        # the fragment the page builder inlines: colours come from the stylesheet
        # so the mark follows the theme, including on paper
        "tools/mark.svg": (lozenge(25.5, "currentColor", 2.6, cls="mk-rule")
                           + n(600, 23, "currentColor", cls="mk-letter") + "\n"),
    }


def pack_ico():
    """Bundle the rendered 16, 32 and 48 pixel icons into favicon.ico."""
    from PIL import Image
    sizes = (16, 32, 48)
    parts = [ROOT / "assets" / f"tmp-favicon-{s}.png" for s in sizes]
    missing = [p.name for p in parts if not p.exists()]
    if missing:
        sys.exit("run `node tools/rasterise.mjs` first, missing: " + ", ".join(missing))
    images = [Image.open(p).convert("RGBA") for p in parts]
    images[-1].save(ROOT / "favicon.ico", format="ICO",
                    sizes=[(s, s) for s in sizes], append_images=images[:-1])
    for p in parts:
        p.unlink()
    print(f"favicon.ico packed at {', '.join(str(s) for s in sizes)}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="fail if a file is out of date")
    ap.add_argument("--ico", action="store_true",
                    help="pack favicon.ico from the PNGs tools/rasterise.mjs rendered")
    args = ap.parse_args()
    if args.ico:
        return pack_ico()
    stale = []
    for rel, body in files().items():
        path = ROOT / rel
        current = path.read_text() if path.exists() else None
        if current == body:
            continue
        if args.check:
            stale.append(rel)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(body)
            print(f"wrote {rel}")
    if args.check:
        if stale:
            sys.exit("out of date: " + ", ".join(stale))
        print(f"{len(files())} logo files up to date")


if __name__ == "__main__":
    main()
