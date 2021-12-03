import fontforge
from pathlib import Path

font = fontforge.font() # new font

svgFilePaths = list(Path('SVG').glob('**/*.svg'))

for p in svgFilePaths:
	dec = p.stem.split(" ", 1)[0]
	glyph = font.createChar(int(dec))
	glyph.importOutlines(str(p))


name = 'SbsSlim'

# How to set the font name? http://lk4.us/fLbY4
font.fontname = f"{name}-Regular"
font.fullname = f"{name} Regular"
font.familyname = f"{name}"
font.save('output.sfd')

font.generate(f'{name}.otf')
font.generate(f'{name}.ttf')
font.generate(f'{name}.woff')
font.generate(f'{name}.woff2')
