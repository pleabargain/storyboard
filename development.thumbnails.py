from PIL import Image
import glob, os

# usage
# enter the full path of the target directory with your images.
# when you run the script all images in the directory will be forced to resize 
# expect distortion in the output!

# size = 150, 150

# for infile in glob.glob("*.jpg"):
# declare full path to the image directory

#TODO create a function call?

for infile in glob.glob("/home/dgd/Desktop/python_storyboard_flashcards/random_images/*.*"):
    file, ext = os.path.splitext(infile)
    print(file,ext)
    #ignore already processed
    if "_thumbnail" in file:
        continue
    if ext.lower() in [".jpg",".png",".jpeg",]:
        # TODO if .svg call SVG parser to convert to png first
        
        with Image.open(infile) as im:
            #change these values to match your file size image need
            new_image= im.resize((150,150))
            new_image.save(file + "_thumbnail.png", "PNG")


