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
	glyph.width=450
	#print(glyph.width)


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
sample_text = """

 	!	"	#	$	%	&	'	(	)	*	+	,	-	.	/
0	1	2	3	4	5	6	7	8	9	:	;	<	=	>	?
@	A	B	C	D	E	F	G	H	I	J	K	L	M	N	O
P	Q	R	S	T	U	V	W	X	Y	Z	[	\	]	^	_
`	a	b	c	d	e	f	g	h	i	j	k	l	m	n	o
p	q	r	s	t	u	v	w	x	y	z	{	|	}	~	
 	¡	¢	£	¤	¥	¦	§	¨	©	ª	«	¬	­	®	¯
°	±	²	³	´	µ	¶	·	¸	¹	º	»	¼	½	¾	¿
À	Á	Â	Ã	Ä	Å	Æ	Ç	È	É	Ê	Ë	Ì	Í	Î	Ï
Ð	Ñ	Ò	Ó	Ô	Õ	Ö	×	Ø	Ù	Ú	Û	Ü	Ý	Þ	ß
à	á	â	ã	ä	å	æ	ç	è	é	ê	ë	ì	í	î	ï
ð	ñ	ò	ó	ô	õ	ö	÷	ø	ù	ú	û	ü	ý	þ	ÿ

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

------
#include <iostream>
using namespace std;

int main() {
  cout << "Hello World!";
  return 0;
}
"""
font.printSample('fontsample', (12, 16, 24, 36), sample_text, 'sample.pdf')

from pdf2image import convert_from_path
 
 
# Store Pdf with convert_from_path function
images = convert_from_path('sample.pdf')
for i in range(len(images)):
    images[i].save('page'+ str(i) +'.jpg', 'JPEG')
