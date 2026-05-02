from pathlib import Path
import textwrap

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
FONT_PATH = ROOT / "SbsSlim.ttf"
TEST_DIR = ROOT / "test"
OUTPUT_PATH = TEST_DIR / "article_specimen.jpg"


ARTICLE = """
Regular type should disappear while a reader follows the argument. In a programming font, that ordinary reading test still matters because comments, documentation, commit messages, logs, and terminal output are mostly prose. The letters need to hold a steady rhythm across long lines, not only inside short alphabet specimens. A word like regular should feel even, and repeated shapes in minimum, millennium, language, debugging, and configuration should not create accidental gaps.

The same font must also survive dense technical notation. A developer scans names such as request_handler, cache_key, glyph_metrics, and render_spacing_specimen while also reading operators like !=, ==, <=, >=, ->, =>, &&, ||, ::, and ... . Those marks need enough presence to be found quickly, but they should not pull the whole line darker than the surrounding words. Brackets and braces should frame expressions without looking like stray fence posts.

Spacing is especially visible around letters with open sides. The combinations eg, ge, gu, ug, re, ar, ra, ul, lu, la, al, and ill can reveal whether a glyph is sitting too far left or right in its cell. Round letters need optical side bearings, vertical stems need consistent weight, and descenders should leave a clean path through the line below. When g, u, r, n, m, and w share a sentence, their stems should look like members of one family.

Here is a realistic terminal paragraph: warning: package lock changed after install; run tests before pushing. info: cached 42 modules in ./build/cache. error: expected value != null at src/parser/state.ts:128. Success should read clearly too: check passed, coverage >= 90%, deploy ready -> staging.

Small symbols are part of the texture as well. A CLI might print ✓ build completed, ✗ tests failed, ⚠ config missing, ★ release candidate, ℹ help available, or arrows such as ← ↑ → ↓ to show navigation. Even if these are monochrome fallbacks, they should align with the text around them and avoid shouting unless the symbol is intentionally heavy.

The final judgment is not one perfect metric. It is the combined effect of spacing, stroke weight, counters, tails, punctuation, and line rhythm over several paragraphs. If a page like this feels calm, readable, and predictable, the individual glyph decisions are probably moving in the right direction.
""".strip()


CODE_LINES = [
    "function normalizeGlyph(name, metrics) {",
    "  const ok = metrics.left >= 45 && metrics.right >= -20;",
    "  return ok ? metrics.centerDelta : metrics.centerDelta + 1;",
    "}",
    "git status --short && npm test -- --runInBand",
]


def wrap_paragraph(draw, text, font, max_width):
    words = text.split()
    lines = []
    line = ""
    for word in words:
        candidate = f"{line} {word}".strip()
        if draw.textlength(candidate, font=font) <= max_width:
            line = candidate
        else:
            if line:
                lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def main():
    TEST_DIR.mkdir(exist_ok=True)
    body_font = ImageFont.truetype(str(FONT_PATH), 42)
    code_font = ImageFont.truetype(str(FONT_PATH), 38)
    title_font = ImageFont.truetype(str(FONT_PATH), 64)
    label_font = ImageFont.truetype(str(FONT_PATH), 26)

    width = 1800
    margin_x = 150
    y = 90
    line_height = 58
    paragraph_gap = 28
    max_width = width - margin_x * 2

    scratch = Image.new("RGB", (width, 100), "white")
    scratch_draw = ImageDraw.Draw(scratch)

    paragraphs = ARTICLE.split("\n\n")
    wrapped = [wrap_paragraph(scratch_draw, paragraph, body_font, max_width) for paragraph in paragraphs]
    text_height = 120 + sum(len(lines) * line_height + paragraph_gap for lines in wrapped)
    code_height = len(CODE_LINES) * 48 + 76
    height = text_height + code_height + 120

    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    draw.text((margin_x, y), "SbsSlim Article Specimen", fill="black", font=title_font)
    y += 92
    draw.text((margin_x, y), "Long prose, operators, symbols, and code-text spacing", fill=(110, 110, 110), font=label_font)
    y += 70

    for lines in wrapped[:3]:
        for line in lines:
            draw.text((margin_x, y), line, fill="black", font=body_font)
            y += line_height
        y += paragraph_gap

    code_top = y + 8
    draw.rectangle((margin_x - 22, code_top - 18, width - margin_x + 22, code_top + code_height - 18), outline=(210, 210, 210), width=2)
    draw.text((margin_x, code_top), "Code Texture", fill=(110, 110, 110), font=label_font)
    y = code_top + 50
    for line in CODE_LINES:
        draw.text((margin_x, y), line, fill="black", font=code_font)
        y += 48
    y += paragraph_gap

    for lines in wrapped[3:]:
        for line in lines:
            draw.text((margin_x, y), line, fill="black", font=body_font)
            y += line_height
        y += paragraph_gap

    image.save(OUTPUT_PATH, quality=95)
    print(f"wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
