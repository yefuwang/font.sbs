import fontforge
from pathlib import Path

font = fontforge.font() # new font

svgFilePaths = list(Path('SVG').glob('**/*.svg'))

for p in svgFilePaths:
	dec = p.stem.split(" ", 1)[0]
	glyph = font.createChar(int(dec))
	glyph.importOutlines(str(p))
	glyph.left_side_bearing=60
	glyph.right_side_bearing=60


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

# print samples
fontforge.printSetup('pdf-file', 'z.pdf', 600, 200)
font.selection.select(("unicode","ranges"),ord('A'),ord('Z'))
font.printSample('fontsample', (12, 16, 24, 36), 'abcdefghijklmnokqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\n1lI\noO0', 'sample.pdf')

from pdf2image import convert_from_path
 
 
# Store Pdf with convert_from_path function
images = convert_from_path('sample.pdf')
for i in range(len(images)):
    images[i].save('page'+ str(i) +'.jpg', 'JPEG')