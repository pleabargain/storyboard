from PIL import Image
import glob, os
import re

from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM


# TODO not all svg are being processed. e.g. /home/dgd/Desktop/python_storyboard_flashcards/random_images/noun_insect_caterpillar.svg

# usage
# enter the full path of the target directory with your images.
# when you run the script all images in the directory will be forced to resize 
# expect distortion in the output!

# size = 150, 150

# for infile in glob.glob("*.jpg"):
# declare full path to the image directory

#TODO create a function call?
search_text = "<svg"
  
#Creating a variable and storing
# the text that we want to update
replace_text = """<svg width="150px" height="150px" """

folder_name = "/home/dgd/Desktop/python_storyboard_flashcards/random_images/"

for infile in glob.glob(folder_name + "*.*"):
    file, ext = os.path.splitext(infile)
    print(file,ext)
    #ignore already processed
    # if "_thumbnail" in file:
    #     continue
    if ext.lower() in [".svg",]:
        #                 ".jpg",
        #                 ".png",
        #                 ".jpeg",]:
        # # TODO if .svg call SVG parser to convert to png first

        # if ext.lower() == '.svg':
            newlines=[]
            with open(infile) as f:
                lines = f.readlines()
            for line in lines:
                if search_text in line and replace_text not in line:
                    line2 = line.replace(search_text,replace_text)
                    newlines.append(line2)
                else:
                    newlines.append(line)
            with open(infile,"w") as f:
                f.writelines(newlines)
            
            drawing = svg2rlg(infile)
            renderPM.drawToFile(drawing, file+'.png', fmt='PNG')

for infile in glob.glob(folder_name +"*.*"):

    file, ext = os.path.splitext(infile)
    print(file,ext)
    #ignore already processed
    if "_thumbnail" in file:
        continue
    if ext.lower() in [".jpg",
                       ".png",
                       ".jpeg",]:

        with Image.open(infile) as im:
            #change these values to match your file size image need
            new_image= im.resize((150,150))
            new_image.save(file + "_thumbnail.png", "PNG")


