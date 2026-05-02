# SbsSlim Glyph Design

This document defines the cleaner, more systematic drawing model for new glyphs. The existing SVG files remain useful references, but new work should prefer these shared constants over one-off Illustrator artifacts.

## Canvas

All glyph source SVGs use a fixed `18 x 35` viewBox:

```svg
viewBox="0 0 18 35"
```

Use `#231f20` for filled shapes. Avoid strokes in source SVGs when possible; prefer filled paths, rectangles, and ellipses so FontForge imports outlines predictably.

## Vertical Metrics

```text
CAP_TOP = 3
ASCENDER_TOP = 3
X_HEIGHT = 10
BASELINE = 28
DESCENDER_BOTTOM = 35
OPERATOR_CENTER = 17.5
ACCENT_TOP = 3
ACCENT_BOTTOM = 8
```

Uppercase glyphs normally occupy `y=3..28`. Lowercase x-height glyphs occupy `y=10..28`. Descenders may extend to `y=35`.

## Horizontal Metrics

```text
LEFT_EDGE = 2
RIGHT_EDGE = 16
CENTER = 9
NORMAL_LEFT_STEM = 3
NORMAL_RIGHT_STEM = 13
```

The build gives every glyph the same advance width, but preserves the horizontal placement from the SVG viewBox. Keep the visible drawing narrow and centered unless the glyph intentionally needs optical correction. Do not rely on the build script to normalize side bearings; adjust the SVG position instead.

After FontForge import, most glyphs should also stay optically balanced inside the monospaced advance. Use `tools/glyph_metrics.py` to inspect imported bounds:

```text
NORMAL_CENTER_DELTA = 20..40 font units
NARROW_CENTER_DELTA = 0..35 font units
ASYMMETRIC_CENTER_DELTA = up to 50 font units
REVIEW_CENTER_DELTA = over 55 font units
NORMAL_RIGHT_BEARING = 0..40 font units
ALLOWED_RIGHT_OVERHANG = down to -15 font units
REVIEW_RIGHT_OVERHANG = below -20 font units
```

These are review thresholds, not rigid laws. Use the rendered spacing specimen as the final judge. Terminal box and block elements are excluded from these normal optical-spacing rules because they must connect to the full cell.

## Stroke Weights

```text
PRIMARY_STROKE = 2.0
LIGHT_STROKE = 1.5
HEAVY_STROKE = 3.0
STEM_TOLERANCE = 0.25
DOT_RX = 1.77
DOT_RY = 1.82
```

Use `PRIMARY_STROKE` for most stems, bars, diagonals, digit strokes, and operator strokes. Use `LIGHT_STROKE` for small details, inner joins, and accents when a full primary stroke would clog the form. Use `HEAVY_STROKE` for bracket-like symbols, strong vertical punctuation, and terminal UI symbols.

The goal is perceived consistency, not mathematical sameness. Curves, diagonals, and tiny details may need optical correction, but glyphs in the same family should appear to have the same weight. For example, lowercase stem glyphs such as `n`, `h`, `u`, `m`, and `r` should not alternate between visibly thin and visibly heavy stems without a reason.

Default stroke expectations:

```text
vertical stems: usually 2.0
horizontal bars: usually 2.0
diagonals: usually 2.0, slightly heavier only if they look light
curved bowls: visually match a 2.0 stem
small accents: 1.5..2.0
dots: standard dot ellipse unless the glyph family requires otherwise
brackets and terminal symbols: 2.0..3.0 depending on role
```

Review any normal text glyph with structural strokes outside `PRIMARY_STROKE +/- STEM_TOLERANCE` unless the difference is an intentional optical correction.

## Shape Rules

New glyphs should be systematic, narrow, and coding-focused:

- Use rectangles for straight stems and bars.
- Use rotated rectangles or simple filled polygons for diagonals.
- Use smooth oval-like paths for bowls.
- Keep counters open and readable.
- Use blunt terminals.
- Keep curves restrained; avoid decorative tails.
- Prefer reusable components for accents and related symbols.

Avoid mixing two design languages in the same family. Older Illustrator glyphs may be irregular; new and revised glyphs should move toward the systematic rules in this document while preserving the ultra-narrow identity of the font.

## Family Normalization

Review and edit related glyphs as families rather than isolated one-offs.

Lowercase stem family:

```text
i j l f t h n m u r
```

These should share stem weight, vertical alignment, and optical centering logic.

Round lowercase family:

```text
a b c d e g o p q
```

These should share bowl weight, counter openness, x-height, and baseline behavior.

Uppercase stem family:

```text
B D E F H I K L M N P R T U
```

These should share cap height, primary stroke weight, and interior spacing.

Digits:

```text
0 1 2 3 4 5 6 7 8 9
```

Digits should feel stable in tables, logs, version numbers, and line numbers. Normalize them as a group before making isolated digit changes. Priorities are consistent visual width, consistent center, no large right overhang, and clear distinctions between `0/O`, `1/l/I`, `5/S`, and `8/B`.

Operators:

```text
+ - = < > * / \ | & ^ % # ~ ! ? : ; . , _
```

Coding operators should be readable but should not dominate adjacent letters or digits. Normalize stroke weight and optical alignment as a group.

Brackets:

```text
() [] {}
```

Bracket families should align visually with each other. Left and right forms should mirror in weight and vertical placement even when their optical centers differ.

## Component Rules

Common components should be reused:

```text
vertical stem
horizontal bar
diagonal slash
oval bowl
half bowl
standard dot
comma tail
acute
grave
circumflex
tilde
dieresis
cedilla
```

Accented glyphs should be generated or drawn as base glyph plus a positioned accent whenever possible.

## Terminal UI Rules

Box-drawing glyphs are allowed to use the full cell instead of the normal visual margins. They must connect across adjacent terminal cells.

```text
BOX_CENTER_X = 9
BOX_CENTER_Y = 17.5
BOX_LIGHT_STROKE = 2
BOX_LIGHT_VERTICAL_X = 8
BOX_LIGHT_HORIZONTAL_Y = 16.5
```

Horizontal box strokes should run to `x=0` or `x=18` when they connect left or right. Vertical box strokes should run to `y=0` or `y=35` when they connect up or down.

Block elements also use the full cell. Half blocks split at `x=9` or `y=17.5`. Shade blocks use a fixed rectangular dot pattern so they remain readable in a very narrow cell.

## Starter Prototypes

These glyphs establish the first systematic additions:

- `U+0020 space`: metrics-only glyph with no outlines.
- `U+00A6 brokenbar`: centered heavy vertical symbol split around the operator center.
- `U+00B7 middot`: standard dot centered at `OPERATOR_CENTER`.
