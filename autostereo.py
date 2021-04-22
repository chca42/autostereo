#!/usr/bin/python

import sys
import os.path
import random
import math
from PIL import Image

fin = sys.argv[1]
fout = os.path.basename(fin) + "-enc.jpg"

imPattern = Image.open("pattern.jpg")
imPatternSize = imPattern.size

imDepth = Image.open(fin)
imDepthSize = imDepth.size
factorY = imPatternSize[1] / float(imDepthSize[1])
imDepthSize = (int(imDepthSize[0]*factorY), int(imDepthSize[1]*factorY))
imDepth = imDepth.resize(imDepthSize, Image.ANTIALIAS)

size = ( imDepthSize[0], imPatternSize[1] )
im = Image.new("RGB", size)

stripWidth = imPatternSize[0]

for i in range(0,size[0]):
	for j in range(0,size[1]):
		if i < stripWidth:
			colour = imPattern.getpixel((i,j))
			im.putpixel((i,j), colour)
		elif i > stripWidth and (i-stripWidth) < imDepthSize[0] and j < imDepthSize[1]:
			height = int(imDepth.getpixel((i-stripWidth,j))/255.0*(imPatternSize[0]/2))
			colour = im.getpixel((i-stripWidth+height, j))
		else:
			colour = im.getpixel((i-stripWidth, j))
		im.putpixel((i,j), colour)

im.save(fout)

