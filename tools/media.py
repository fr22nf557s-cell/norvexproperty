#!/usr/bin/env python3
"""Build the responsive image ladder for the site.

Masters live in assets/master/ (4K frames cut from the film master; they are
deliberately NOT committed, see .gitignore). For every master this writes an
AVIF and WebP ladder into assets/img/ plus a JPEG fallback at 1920, and records
what it produced in assets/img/manifest.json so the page builder can only ever
reference files that exist.

    python3 tools/media.py            # build everything that is missing
    python3 tools/media.py --force    # rebuild every size

Requires Pillow (>=11) with AVIF and WebP support.
"""
import json
import os
import sys

from PIL import Image, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MASTERS = os.path.join(ROOT, "assets", "master")
OUT = os.path.join(ROOT, "assets", "img")

# One ladder serves both jobs: a full-bleed hero picks the top of it, an
# insight card near the bottom. AVIF carries the 4K step; WebP stops at 2560
# because the browsers that still need it are not on 4K panels.
AVIF_WIDTHS = (640, 1280, 1920, 2560, 3840)
WEBP_WIDTHS = (640, 1280, 1920, 2560)
JPEG_WIDTH = 1920  # fallback src, Open Graph, and any client without <picture>

# A 9:16 master is only ever shown on a phone held upright, so its ladder stops
# where phones do rather than following the landscape one.
PORTRAIT_AVIF = (480, 720, 1080, 1216)
PORTRAIT_WEBP = (480, 720, 1080)
PORTRAIT_JPEG = 1080

# Smaller sizes get a touch more quality: they are cheap and they are what
# most phones actually download.
def avif_quality(w):
    # Raised across the ladder: these are the stills people look at while they
    # read, and AVIF is cheap enough that shaving them was a false economy.
    return 78 if w <= 640 else 74 if w <= 1280 else 70 if w <= 1920 else 66


def webp_quality(w):
    return 88 if w <= 640 else 85 if w <= 1280 else 80


def resize(im, w):
    if im.width == w:
        return im.copy()
    h = round(im.height * w / im.width)
    out = im.resize((w, h), Image.LANCZOS)
    # Lanczos leaves a downscale very slightly soft; a light unsharp mask puts
    # the edge definition back without haloing. Strength tapers off as the
    # output approaches the master's own resolution.
    ratio = w / im.width
    if ratio < 0.95:
        percent = 60 if ratio < 0.4 else 45 if ratio < 0.7 else 32
        out = out.filter(ImageFilter.UnsharpMask(radius=0.7, percent=percent, threshold=3))
    return out


def build(path, force=False):
    name = os.path.splitext(os.path.basename(path))[0]
    master = Image.open(path)
    if master.mode != "RGB":
        master = master.convert("RGB")
    made, sizes = [], {"avif": [], "webp": []}
    portrait = master.height > master.width
    avif_widths = PORTRAIT_AVIF if portrait else AVIF_WIDTHS
    webp_widths = PORTRAIT_WEBP if portrait else WEBP_WIDTHS
    jpeg_width = PORTRAIT_JPEG if portrait else JPEG_WIDTH

    for w in avif_widths:
        if w > master.width:
            continue
        dst = os.path.join(OUT, f"{name}-{w}.avif")
        sizes["avif"].append(w)
        if force or not os.path.exists(dst):
            resize(master, w).save(dst, "AVIF", quality=avif_quality(w), speed=4,
                                   subsampling="4:2:0" if w > 1920 else "4:4:4")
            made.append(os.path.basename(dst))

    for w in webp_widths:
        if w > master.width:
            continue
        dst = os.path.join(OUT, f"{name}-{w}.webp")
        sizes["webp"].append(w)
        if force or not os.path.exists(dst):
            resize(master, w).save(dst, "WEBP", quality=webp_quality(w), method=6)
            made.append(os.path.basename(dst))

    dst = os.path.join(OUT, f"{name}.jpg")
    if force or not os.path.exists(dst):
        # Only browsers without <picture> or AVIF and WebP ever fetch this, plus
        # the social preview, so it does not need the 4:4:4 treatment.
        resize(master, min(jpeg_width, master.width)).save(
            dst, "JPEG", quality=82, optimize=True, progressive=True)
        made.append(os.path.basename(dst))

    return name, {"w": master.width, "h": master.height, **sizes}, made


def main():
    force = "--force" in sys.argv
    if not os.path.isdir(MASTERS):
        sys.exit(f"no masters in {MASTERS} - fetch them first (see README)")
    os.makedirs(OUT, exist_ok=True)
    manifest, total = {}, 0
    for f in sorted(os.listdir(MASTERS)):
        if not f.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
            continue
        name, entry, made = build(os.path.join(MASTERS, f), force)
        manifest[name] = entry
        total += len(made)
        print(f"{name}: {entry['w']}x{entry['h']} master, {len(made)} file(s) written")
    with open(os.path.join(OUT, "manifest.json"), "w") as fh:
        json.dump(manifest, fh, indent=1, sort_keys=True)
        fh.write("\n")
    print(f"{len(manifest)} image(s), {total} file(s) written, manifest updated")


if __name__ == "__main__":
    main()
