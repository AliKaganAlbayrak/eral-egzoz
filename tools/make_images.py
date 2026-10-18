"""Generates the social share image (og-image.png) and the touch icon (apple-touch-icon.png).

Usage:
    pip install pillow
    python tools/make_images.py

Uses Impact and Arial Bold from Windows when available, falling back to DejaVu fonts.
"""

from __future__ import annotations

import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "img"

RED = (215, 23, 31)
RED_DARK = (167, 15, 21)
DARK = (18, 20, 24)
YELLOW = (255, 214, 10)
WHITE = (255, 255, 255)
GREY = (190, 195, 202)


def font(names: list[str], size: int) -> ImageFont.FreeTypeFont:
    dirs = [Path("C:/Windows/Fonts"), Path("/usr/share/fonts/truetype/dejavu"), Path("/Library/Fonts")]
    for name in names:
        for d in dirs:
            p = d / name
            if p.exists():
                return ImageFont.truetype(str(p), size)
    return ImageFont.load_default()


def save(img: Image.Image, name: str) -> None:
    path = OUT / name
    if os.name == "nt":
        path = Path("\\\\?\\" + str(path.resolve()))
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path, optimize=True)
    print("  wrote: assets/img/" + name)


def exhaust_mark(d: ImageDraw.ImageDraw, x: int, y: int, s: float, color=WHITE) -> None:
    """Draws the exhaust logo mark (designed on a 32x32 grid)."""
    w = max(2, round(2.2 * s))
    P = lambda a, b: (x + a * s, y + b * s)  # noqa: E731
    d.line([P(2, 20), P(4.5, 19.5), P(6.5, 17), P(9, 16)], fill=color, width=w, joint="curve")
    d.rounded_rectangle([P(8, 10), P(22, 21)], radius=5 * s, outline=color, width=w)
    d.line([P(22, 15.5), P(27, 15.5)], fill=color, width=w)
    d.line([P(27, 12.5), P(27, 18.5)], fill=color, width=w)


def og_image() -> None:
    W, H = 1200, 630
    img = Image.new("RGB", (W, H), DARK)
    d = ImageDraw.Draw(img)
    # background grid
    for gx in range(0, W, 40):
        d.line([(gx, 0), (gx, H)], fill=(28, 31, 36))
    for gy in range(0, H, 40):
        d.line([(0, gy), (W, gy)], fill=(28, 31, 36))
    # red diagonal panels on the right
    d.polygon([(840, 0), (W, 0), (W, H), (720, H)], fill=RED)
    d.polygon([(1010, 0), (W, 0), (W, H), (900, H)], fill=RED_DARK)
    # logo mark
    d.rounded_rectangle([830, 205, 1050, 425], radius=36, fill=WHITE)
    exhaust_mark(d, 845, 222, 6.0, color=RED)

    impact = ["impact.ttf", "DejaVuSans-Bold.ttf"]
    bold = ["arialbd.ttf", "DejaVuSans-Bold.ttf"]
    # yellow name tag
    tag_font = font(impact, 52)
    tag = "GÜMÜŞHANELİLER"
    tb = d.textbbox((0, 0), tag, font=tag_font)
    d.rectangle([70, 110, 70 + tb[2] - tb[0] + 36, 110 + 80], fill=YELLOW, outline=(0, 0, 0), width=3)
    d.text((88, 118 - tb[1] + 6), tag, font=tag_font, fill=(0, 0, 0))
    # wordmark
    d.text((66, 190), "EGZOZ", font=font(impact, 190), fill=RED)
    # tagline, address and phone
    d.text((72, 430), "Egzoz · Katalizatör · DPF Temizliği", font=font(bold, 38), fill=WHITE)
    d.text((72, 486), "Fatih Oto Sanayi Sitesi, Esenyurt / İstanbul", font=font(bold, 30), fill=GREY)
    d.text((72, 536), "0537 463 88 38", font=font(bold, 34), fill=YELLOW)
    save(img, "og-image.png")


def touch_icon() -> None:
    S = 180
    img = Image.new("RGB", (S, S), RED)
    d = ImageDraw.Draw(img)
    exhaust_mark(d, 6, 6, 5.25)
    save(img, "apple-touch-icon.png")


if __name__ == "__main__":
    og_image()
    touch_icon()
