import fontforge
from pathlib import Path

font = fontforge.font() # new font

svgFilePaths = list(Path('SVG').glob('**/*.svg'))

for p in svgFilePaths:
	dec = p.stem.split(" ", 1)[0]
	glyph = font.createChar(int(dec))
	glyph.importOutlines(str(p))

font.save('output.sfd')

name = 'sbsthin'

font.generate(f'{name}.otf')
font.generate(f'{name}.ttf')
font.generate(f'{name}.woff')
font.generate(f'{name}.woff2')
