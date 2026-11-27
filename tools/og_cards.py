#!/usr/bin/env python3
"""Make link-preview cards (og:image, 1200x630 JPEG) for the pages listed in data/og.json.

    python3 tools/og_cards.py                 # writes static/og/<slug>.jpg
    python3 tools/og_cards.py --defaults DIR  # site-wide default card candidates (previews only, not published)

Needs Pillow (build.py does not). Each card is a crop of the photo file the page already shows, so any
face blur or crop recorded in data/photos.json is kept. The photo's attribution line is written into the
JPEG's EXIF (Artist / Copyright / ImageDescription); the page that shows the photo carries the visible credit.
Published photos are at most 780px wide, so cards are scaled up about 1.5x (LANCZOS + light sharpening).
"""
import json, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parent.parent
W, H = 1200, 630


def registry():
    reg = {}
    for x in json.loads((ROOT / "data/photos.json").read_text(encoding="utf-8")):
        reg[x["file"]] = x
    return reg


def crop(im, focus=0.5):
    """Largest W:H box, centred horizontally, vertical centre at `focus` (0 top, 1 bottom), then scale to WxH."""
    im = im.convert("RGB")
    w, h = im.size
    if w / h > W / H:  # too wide: trim the sides
        cw, ch = round(h * W / H), h
        x, y = (w - cw) // 2, 0
    else:
        cw, ch = w, round(w * H / W)
        y = min(max(round(focus * h - ch / 2), 0), h - ch)
        x = 0
    out = im.crop((x, y, x + cw, y + ch)).resize((W, H), Image.LANCZOS)
    return out.filter(ImageFilter.UnsharpMask(radius=1.2, percent=60, threshold=2))


def exif_for(entry):
    ex = Image.Exif()
    credit = entry.get("attribution") or f'Photo: {entry.get("author", "")}, {entry.get("license", "")}'
    credit = credit.encode("ascii", "replace").decode()
    ex[0x013B] = credit[:200]                       # Artist
    ex[0x8298] = credit                             # Copyright
    ex[0x010E] = f'{credit} | source: {entry.get("source_url", "")} | link-preview crop by Nadri'.encode("ascii", "replace").decode()
    return ex


def save(im, path, exif=None):
    path.parent.mkdir(parents=True, exist_ok=True)
    kw = {"quality": 85, "optimize": True, "progressive": True}
    if exif is not None:
        kw["exif"] = exif
    im.save(path, "JPEG", **kw)
    return path.stat().st_size


def pages():
    cfg = json.loads((ROOT / "data/og.json").read_text(encoding="utf-8"))["pages"]
    reg = registry()
    for slug, c in cfg.items():
        entry = reg.get(c["photo"])
        if not entry:
            raise SystemExit(f"{c['photo']} is not in data/photos.json (license not recorded)")
        card = crop(Image.open(ROOT / c["photo"]), c.get("focus", 0.5))
        size = save(card, ROOT / "static/og" / f"{slug}.jpg", exif_for(entry))
        print(f"static/og/{slug}.jpg  {size // 1024} KB  <- {c['photo']} ({entry['license']})")


# ---------- default card candidates (owner picks one; not published by this tool) ----------
def bezier(p0, p1, p2, p3, n=24):
    return [tuple((1 - t) ** 3 * a + 3 * (1 - t) ** 2 * t * b + 3 * (1 - t) * t ** 2 * c + t ** 3 * d
                  for a, b, c, d in zip(p0, p1, p2, p3)) for t in (i / n for i in range(n + 1))]


def mark(size):
    """static/nadri-mark-light.svg redrawn with the same coordinates (64x64 viewBox), 4x supersampled."""
    S = 4 * size / 64
    big = Image.new("RGBA", (4 * size, 4 * size), (0, 0, 0, 0))
    d = ImageDraw.Draw(big)
    import math
    cx, cy, a = 32, 36, math.radians(45)
    rot = lambda x, y: (cx + (x - cx) * math.cos(a) - (y - cy) * math.sin(a), cy + (x - cx) * math.sin(a) + (y - cy) * math.cos(a))
    for x, y, col in [(13, 17, "#5E9C8B"), (33, 17, "#F0B93A"), (13, 37, "#9DC3E6"), (33, 37, "#9C3D63")]:
        d.polygon([tuple(v * S for v in rot(px, py)) for px, py in [(x, y), (x + 18, y), (x + 18, y + 18), (x, y + 18)]], fill=col)
    pts = (bezier((24, 9), (28, 3), (32, 9), (32, 11)) + bezier((32, 11), (32, 9), (36, 3), (40, 9))
           + bezier((40, 9), (37, 12), (34, 12), (32, 11)) + bezier((32, 11), (30, 12), (27, 12), (24, 9)))
    d.polygon([(x * S, y * S) for x, y in pts], fill="#efe9dd")
    return big.resize((size, size), Image.LANCZOS)


def default_card(photo, focus, catch, out):
    reg = registry()
    card = crop(Image.open(ROOT / photo), focus).convert("RGBA")
    # bottom scrim so the type reads on any photo
    scrim = Image.new("L", (1, H))
    for y in range(H):
        scrim.putpixel((0, y), int(max(0, (y - H * 0.42) / (H * 0.58)) ** 1.3 * 200))
    shade = Image.new("RGBA", (W, H), (12, 14, 18, 255))
    shade.putalpha(scrim.resize((W, H)))
    card = Image.alpha_composite(card, shade)
    head = ImageFont.truetype(str(ROOT / "static/fonts/song-myung-latin-400-normal.woff2"), 108)
    text = ImageFont.truetype(str(ROOT / "static/fonts/ibm-plex-sans-kr-latin-600-normal.woff2"), 38)
    small = ImageFont.truetype(str(ROOT / "static/fonts/ibm-plex-sans-kr-latin-400-normal.woff2"), 24)
    m = mark(112)
    card.alpha_composite(m, (64, H - 64 - 112 - 58))
    d = ImageDraw.Draw(card)
    d.text((64 + 112 + 22, H - 64 - 58 - 8), "Nadri", font=head, fill="#f6f1e7", anchor="ls")
    d.text((66, H - 64), catch, font=text, fill="#f6f1e7", anchor="ls")
    d.text((W - 48, H - 66), "nadri-guide.pages.dev", font=small, fill=(246, 241, 231, 200), anchor="rs")
    size = save(card.convert("RGB"), out, exif_for(reg[photo]))
    print(f"{out}  {size // 1024} KB  <- {photo} ({reg[photo]['license']})")


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "--defaults":
        out = Path(sys.argv[2])
        default_card("static/photo/market-1.webp", 0.5, "Less hassle, more joy.", out / "default-A-gwangjang-market.jpg")
        default_card("static/photo/palace-3.webp", 0.5, "Less hassle, more joy.", out / "default-B-changdeokgung.jpg")
    else:
        pages()
