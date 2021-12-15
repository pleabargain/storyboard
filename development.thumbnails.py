from PIL import Image
import glob, os

# size = 150, 150

# for infile in glob.glob("*.jpg"):
# declare full path
for infile in glob.glob("/home/dgd/Desktop/python_storyboard_flashcards/random_images/*.*"):
    file, ext = os.path.splitext(infile)
    print(file,ext)
    #ignore already processed
    if "_thumbnail" in file:
        continue
    if ext.lower() in [".jpg",".png",".jpeg"]:
        
        with Image.open(infile) as im:
         
            new_image= im.resize((150,150))
            new_image.save(file + "_thumbnail.png", "PNG")


