from pathlib import Path


TARGET_RANGES = (
    ("Printable ASCII", range(32, 127)),
    ("Latin-1 supplement", range(160, 256)),
)


def present_codepoints(svg_dir):
    codepoints = set()
    for path in svg_dir.glob("*.svg"):
        codepoint_text = path.stem.split(" ", 1)[0]
        try:
            codepoints.add(int(codepoint_text))
        except ValueError:
            pass
    return codepoints


def describe(codepoint):
    char = chr(codepoint)
    if codepoint == 32:
        char = "space"
    elif char.isspace():
        char = repr(char)
    return f"U+{codepoint:04X} {codepoint:>5} {char}"


def main():
    svg_dir = Path("SVG")
    present = present_codepoints(svg_dir)

    for label, codepoints in TARGET_RANGES:
        missing = [codepoint for codepoint in codepoints if codepoint not in present]
        print(f"{label}: {len(missing)} missing")
        for codepoint in missing:
            print(f"  {describe(codepoint)}")


if __name__ == "__main__":
    main()
