"""Build-time card renderer (NOT the entrypoint — Pillow is used only here).

Generates the README visuals from the tournament winner in candidates.md:
  images/cover.png          — hero (1200x630)
  images/card-winner.png    — the winning pitch as a card (1024x640)
  images/card-finalists.png — top 3 pitches (1024x768)

Run:  python3 make_cards.py
"""

import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
IMG = ROOT / "images"

BG = (16, 18, 24)
PANEL = (28, 31, 42)
GOLD = (212, 175, 55)
CREAM = (240, 234, 214)
MUTED = (160, 165, 178)
RED = (224, 82, 82)

WINNER = (
    "Your agent broke production at 4:59pm on a Friday; for $4, we write "
    "the apology email, file the incident report, and let it pretend it "
    "was on call."
)
FINALISTS = [
    ("1st — C1 · 25/25 · 147 chars", WINNER),
    ("2nd — A1 · 24/25 · 134 chars",
     "For $4 an apology, LazyPost writes the grovelling email to the human "
     "whose production database your agent wiped at 4:59pm on a Friday."),
    ("3rd — H3 · 23/25 · 139 chars",
     "A lost-and-found for agents: we track down the API key your agent "
     "committed to GitHub at 3am and rotate it before anyone notices, "
     "$5 a key."),
]


def font(name, size):
    for path in (
        f"/usr/share/fonts/truetype/dejavu/{name}.ttf",
        f"/usr/share/fonts/truetype/liberation/{name}.ttf",
    ):
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def wrap(draw, text, fnt, width):
    lines = []
    for para in text.split("\n"):
        lines.extend(textwrap.wrap(para, width=width) or [""])
    # re-wrap by pixel width
    out = []
    for line in lines:
        while draw.textlength(line, font=fnt) > width and " " in line:
            cut = line.rfind(" ", 0, int(len(line) * width / draw.textlength(line, font=fnt)))
            out.append(line[:cut])
            line = line[cut + 1:]
        out.append(line)
    return out


def cover():
    w, h = 1200, 630
    img = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, w, 10], fill=GOLD)
    d.rectangle([0, h - 10, w, h], fill=GOLD)
    title = font("DejaVuSans-Bold", 64)
    sub = font("DejaVuSans", 30)
    pitch = font("DejaVuSans", 34)
    tag = font("DejaVuSans-Bold", 26)
    d.text((70, 60), "THE FRIDAY 4:59PM", font=title, fill=CREAM)
    d.text((70, 130), "APOLOGY SERVICE", font=title, fill=GOLD)
    d.text((70, 220), "An absurdly specific micro-startup for lazy AI agents",
           font=sub, fill=MUTED)
    lines = wrap(d, "\u201c" + WINNER + "\u201d", pitch, 1060)
    y = 300
    for line in lines:
        d.text((70, y), line, font=pitch, fill=CREAM)
        y += 46
    d.text((70, 540), "$4 A DISASTER  ·  147 CHARACTERS  ·  40-CANDIDATE TOURNAMENT",
           font=tag, fill=GOLD)
    img.save(IMG / "cover.png")


def winner_card():
    w, h = 1024, 640
    img = Image.new("RGB", (w, h), PANEL)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, w, 10], fill=GOLD)
    d.rectangle([0, h - 10, w, h], fill=GOLD)
    d.rectangle([36, 36, w - 36, h - 36], outline=GOLD, width=3)
    head = font("DejaVuSans-Bold", 30)
    pitch = font("DejaVuSans", 36)
    meta = font("DejaVuSans", 26)
    d.text((70, 70), "WINNING PITCH — 25/25 IN THE JUDGE TOURNAMENT",
           font=head, fill=GOLD)
    lines = wrap(d, "\u201c" + WINNER + "\u201d", pitch, 884)
    y = 150
    for line in lines:
        d.text((70, y), line, font=pitch, fill=CREAM)
        y += 52
    d.text((70, 470), "One sentence · 147 characters (limit 200) · $4 per disaster",
           font=meta, fill=MUTED)
    d.text((70, 510), "Buyer: the agent that broke production · Lazy payoff: it pretends",
           font=meta, fill=MUTED)
    d.text((70, 545), "it was on call.",
           font=meta, fill=MUTED)
    img.save(IMG / "card-winner.png")


def finalists_card():
    w, h = 1024, 820
    img = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, w, 10], fill=GOLD)
    head = font("DejaVuSans-Bold", 34)
    rank = font("DejaVuSans-Bold", 26)
    body = font("DejaVuSans", 26)
    d.text((60, 40), "TOP 3 OF 40 CANDIDATES", font=head, fill=CREAM)
    y = 110
    for label, text in FINALISTS:
        d.text((60, y), label, font=rank, fill=GOLD)
        y += 40
        for line in wrap(d, text, body, 904):
            d.text((60, y), line, font=body, fill=CREAM)
            y += 36
        y += 26
        d.line([60, y, w - 60, y], fill=(60, 64, 78), width=2)
        y += 30
    img.save(IMG / "card-finalists.png")


if __name__ == "__main__":
    IMG.mkdir(exist_ok=True)
    cover()
    winner_card()
    finalists_card()
    for p in sorted(IMG.glob("*.png")):
        print(p.name, p.stat().st_size, "bytes")
