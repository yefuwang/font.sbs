from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
FONT_PATH = ROOT / "SbsSlim.ttf"
TEST_DIR = ROOT / "test"
OUTPUT_PATH = TEST_DIR / "emoji_specimen.jpg"


ROWS = [
    ("Status", "✓ passed    ✔ complete    ✗ failed    ✖ blocked    ⚠ warning    ℹ info"),
    ("Stars", "★ release    ☆ draft    ★★★★★    ☆☆☆☆☆    v1.2.3 ★ stable"),
    ("Arrows", "← previous    ↑ up    → next    ↓ down    ↵ return"),
    ("Objects", "💡 idea    📁 folder    📄 document    📦 package    🔑 key"),
    ("Security", "🔒 locked    🔓 unlocked    🔑 token    ⚠ permission denied"),
    ("Tools", "🔧 configure    🔨 build    🧪 test    📦 publish"),
    ("CLI 1", "✓ install complete  📦 42 packages  🔒 lockfile unchanged"),
    ("CLI 2", "⚠ config missing  💡 try --help  ↵ press return to continue"),
    ("CLI 3", "✗ test failed  🧪 parser.spec.ts  → expected value != null"),
]


GRID = [
    ("✓", "check"),
    ("✔", "heavy check"),
    ("✗", "cross"),
    ("✖", "heavy cross"),
    ("⚠", "warning"),
    ("ℹ", "info"),
    ("★", "black star"),
    ("☆", "white star"),
    ("←", "left"),
    ("↑", "up"),
    ("→", "right"),
    ("↓", "down"),
    ("↵", "return"),
    ("💡", "lightbulb"),
    ("📁", "folder"),
    ("📄", "document"),
    ("📦", "package"),
    ("🔑", "key"),
    ("🔒", "lock"),
    ("🔓", "unlock"),
    ("🔧", "wrench"),
    ("🔨", "hammer"),
    ("🧪", "test tube"),
]


def main():
    TEST_DIR.mkdir(exist_ok=True)
    title_font = ImageFont.truetype(str(FONT_PATH), 64)
    label_font = ImageFont.truetype(str(FONT_PATH), 28)
    row_font = ImageFont.truetype(str(FONT_PATH), 46)
    symbol_font = ImageFont.truetype(str(FONT_PATH), 70)
    caption_font = ImageFont.truetype(str(FONT_PATH), 22)

    width = 1800
    margin_x = 120
    cols = 6
    cell_h = 145
    grid_rows = (len(GRID) + cols - 1) // cols
    height = 70 + 86 + 70 + len(ROWS) * 72 + 30 + 40 + 54 + grid_rows * cell_h + 70

    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    y = 70
    draw.text((margin_x, y), "SbsSlim Emoji and CLI Symbol Specimen", fill="black", font=title_font)
    y += 86
    draw.text((margin_x, y), "Monochrome fallback glyphs mixed with terminal text", fill=(110, 110, 110), font=label_font)
    y += 70

    label_width = 150
    row_height = 72
    for label, text in ROWS:
        draw.text((margin_x, y + 12), label, fill=(120, 120, 120), font=label_font)
        draw.text((margin_x + label_width, y), text, fill="black", font=row_font)
        y += row_height

    y += 30
    draw.line((margin_x, y, width - margin_x, y), fill=(210, 210, 210), width=2)
    y += 40
    draw.text((margin_x, y), "Individual Glyphs", fill=(110, 110, 110), font=label_font)
    y += 54

    cell_w = (width - margin_x * 2) // cols
    for index, (symbol, caption) in enumerate(GRID):
        col = index % cols
        row = index // cols
        x = margin_x + col * cell_w
        top = y + row * cell_h
        draw.rectangle((x, top, x + cell_w - 18, top + cell_h - 18), outline=(220, 220, 220), width=1)
        draw.text((x + 30, top + 14), symbol, fill="black", font=symbol_font)
        draw.text((x + 30, top + 92), caption, fill=(105, 105, 105), font=caption_font)

    image.save(OUTPUT_PATH, quality=95)
    print(f"wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
