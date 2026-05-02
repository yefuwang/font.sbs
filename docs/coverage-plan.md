# SbsSlim Coverage Plan

SbsSlim should stay focused: it is an ultra-narrow programming font, not a general Unicode font. Coverage is organized in layers so each expansion has a clear reason.

## Layer 1: Core Programming

Cover printable ASCII completely:

```text
U+0020..U+007E
```

This layer is required for source code, shells, config files, logs, and plain text.

## Layer 2: Latin-1

Cover Latin-1 Supplement:

```text
U+00A0..U+00FF
```

This supports names, comments, documentation, common western-language text, and the existing specimen in `build_font.py`.

## Layer 3: Programming Typography

Cover common typography used by editors, Markdown, diffs, generated output, and technical docs:

```text
dashes
smart quotes
bullets
ellipsis
prime marks
per mille
fraction slash
minus
```

Initial Layer 3 coverage includes the common dash variants, reversed double quote, prime, and double prime.

## Layer 4: Math And Logic

Prioritize symbols that occur in pseudocode, comments, docs, REPLs, and technical output:

```text
U+2260 not equal
U+2264 less-than or equal
U+2265 greater-than or equal
U+2248 almost equal
U+221E infinity
U+2205 empty set
U+2208 element of
U+2209 not element of
U+221A square root
U+2227 logical and
U+2228 logical or
```

The first Layer 4 batch covers these priority operators.

## Layer 5: Terminal UI

Consider box drawing and block elements after the core glyph system is stable:

```text
U+2500..U+257F Box Drawing
U+2580..U+259F Block Elements
```

These require strict alignment and should be treated as a separate milestone.

The first Layer 5 batch covers the core light box-drawing primitives:

```text
U+2500 light horizontal
U+2502 light vertical
U+250C/U+2510/U+2514/U+2518 light corners
U+251C/U+2524/U+252C/U+2534 light tees
U+253C light crossing
```

The second Layer 5 batch covers core block elements:

```text
U+2580 upper half block
U+2584 lower half block
U+2588 full block
U+258C left half block
U+2590 right half block
U+2591/U+2592/U+2593 shade blocks
```

## Layer 6: CLI Symbols And Emoji Fallbacks

SbsSlim should not try to become a full color emoji font. The practical target is a small monochrome fallback set for common CLI status symbols and selected emoji-like pictograms.

Start with text symbols:

```text
check, cross, warning, info, star, arrows
```

Then add selected emoji code points only when they can read clearly inside the narrow cell:

```text
lock, unlock, key, package, folder, document, wrench, hammer, light bulb, test tube
```

Color emoji may be explored later as a separate experimental build, not as a requirement for the main font.

The first Layer 6 batch covers these text symbols and monochrome emoji fallbacks.

## Current Milestone Order

1. Complete ASCII.
2. Complete Latin-1.
3. Add programming typography gaps.
4. Add math and logic operators.
5. Add terminal box/block symbols.
6. Add curated CLI symbol and emoji fallback glyphs.
