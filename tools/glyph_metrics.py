from pathlib import Path
import unicodedata

import fontforge


ROOT = Path(__file__).resolve().parents[1]
FONT_PATH = ROOT / "output.sfd"

GROUPS = {
    "lowercase": "abcdefghijklmnopqrstuvwxyz",
    "uppercase": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "digits": "0123456789",
    "punctuation": ".,:;!?'\"`-_/\\()[]{}",
    "operators": "+-=<>*/|&^%#~",
}


def glyph_name(char):
    try:
        return unicodedata.name(char)
    except ValueError:
        return "UNNAMED"


def row(font, char):
    glyph = font[ord(char)]
    xmin, ymin, xmax, ymax = glyph.boundingBox()
    width = glyph.width
    ink_width = xmax - xmin
    center = (xmin + xmax) / 2
    target_center = width / 2
    center_delta = center - target_center
    return {
        "char": char,
        "code": f"U+{ord(char):04X}",
        "name": glyph_name(char),
        "width": width,
        "left": xmin,
        "right": xmax,
        "ink": ink_width,
        "center": center,
        "delta": center_delta,
        "lb": glyph.left_side_bearing,
        "rb": glyph.right_side_bearing,
    }


def print_group(font, label, chars):
    print(f"\n[{label}]")
    print("char code    left   right    ink center delta     lb     rb name")
    for char in chars:
        data = row(font, char)
        print(
            f"{data['char']!r:>4} {data['code']:<7}"
            f" {data['left']:>6.1f} {data['right']:>7.1f}"
            f" {data['ink']:>6.1f} {data['center']:>6.1f}"
            f" {data['delta']:>6.1f} {data['lb']:>6.1f}"
            f" {data['rb']:>6.1f} {data['name']}"
        )


def print_outliers(font):
    chars = "".join(GROUPS.values())
    rows = [row(font, char) for char in chars]

    print("\n[widest ink]")
    for data in sorted(rows, key=lambda item: item["ink"], reverse=True)[:12]:
        print(f"{data['char']!r:>4} ink={data['ink']:>6.1f} lb={data['lb']:>6.1f} rb={data['rb']:>6.1f}")

    print("\n[most right-shifted centers]")
    for data in sorted(rows, key=lambda item: item["delta"], reverse=True)[:12]:
        print(f"{data['char']!r:>4} delta={data['delta']:>6.1f} lb={data['lb']:>6.1f} rb={data['rb']:>6.1f}")

    print("\n[most left-shifted centers]")
    for data in sorted(rows, key=lambda item: item["delta"])[:12]:
        print(f"{data['char']!r:>4} delta={data['delta']:>6.1f} lb={data['lb']:>6.1f} rb={data['rb']:>6.1f}")


def main():
    font = fontforge.open(str(FONT_PATH))
    for label, chars in GROUPS.items():
        print_group(font, label, chars)
    print_outliers(font)


if __name__ == "__main__":
    main()
