from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
FONT_PATH = ROOT / "SbsSlim.ttf"
TEST_DIR = ROOT / "test"
OUTPUT_PATH = TEST_DIR / "spacing_grid.jpg"


def main():
    TEST_DIR.mkdir(exist_ok=True)
    font = ImageFont.truetype(str(FONT_PATH), 72)
    label_font = ImageFont.truetype(str(FONT_PATH), 30)
    cell = font.getlength("0")

    lines = [
        ("Words", "Regular regular irregular minimum millennium"),
        ("Pairs", "Re eg ge gu ug ul lu la al ar ra"),
        ("Lower 1", "abcdefghijklmnopqrstuvwxyz"),
        ("Lower 2", "aaa bbb ccc eee ggg iii jjj lll rrr uuu"),
        ("Upper", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
        ("Digits", "0123456789 00 11 22 88 99"),
        ("Punct", ".,:;!? '\"` -_ /\\ () [] {}"),
        ("Ops", "!= == <= >= -> => :: ... && || ++ --"),
        ("Code", "function return class const let var import from"),
        ("Mix", "SbsSlim Regular egeg gugu ill minimum"),
    ]

    left = 300
    row_height = 82
    image = Image.new("RGB", (1900, 920), "white")
    draw = ImageDraw.Draw(image)

    y = 28
    for label, text in lines:
        draw.text((36, y + 16), label, fill=(120, 120, 120), font=label_font)
        for i in range(42):
            x = left + i * cell
            color = (205, 205, 205) if i % 2 == 0 else (230, 230, 230)
            draw.line((x, y - 6, x, y + 72), fill=color, width=1)
        draw.text((left, y), text, fill="black", font=font)
        y += row_height

    image.save(OUTPUT_PATH, quality=95)
    print(f"wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
