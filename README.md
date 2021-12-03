# sbs.slim font

In its current state, sbs.slim is a project for DMA 65 at Irvine Valley College. The author intends to continue this work after the course completes.

## Design Principles

This font is intended to be a coding font for software engineers. The following design choices are made:

* The font should be extremely narrow to allow putting 3 or even 4 columns of code on a common 1080p screen. 
* The font may not be considered legible or beautiful for all audience. Because source codes are not intended to be shared with a fixed typeface, this font is considered successful if a small percentage of users consider it useful.

## Why it is named as sbs.slim?

Because the author bought the domain name https://font.sbs


## Technical Stack

* Use Adobe Illustrator to draw each glyph and export to SVG format.
* Store them under the SVG folder. Each glyph shall be named as [ASCII code][space][description].svg. Only the ASCII code part is significant in font generation. For example, the glyph for A shall be named as "65 A.svg"
* Push the files to this repository. A github action will kick in and run a script to generate the font files (ttf, otf, woff, woff2). The script (build_font.py) is written in python and uses a python library invoking fontforge to generate the font files. (under development at the moment).

## Future work

Finish the full font with some emojis important for software development.


## References

Some code and design procedures referenced Tom Chen's [font-template](https://github.com/tomchen/font-template).
