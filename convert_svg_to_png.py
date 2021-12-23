# resource
# https://clay-atlas.com/us/blog/2021/03/08/python-en-svglib-convert-svg-png/

from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

# TODO loop over the entire directory and parse only the SVG
drawing = svg2rlg('/home/dgd/Desktop/python_storyboard_flashcards/random_images/bikini.svg')
renderPM.drawToFile(drawing, '/home/dgd/Desktop/python_storyboard_flashcards/random_images/bikini.png', fmt='PNG')
