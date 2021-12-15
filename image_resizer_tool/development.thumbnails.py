from PIL import Image
import glob, os

size = 150, 150

# for infile in glob.glob("*.jpg"):
for infile in glob.glob("*.*"):
    file, ext = os.path.splitext(infile)
    print(file,ext)
    #ignore already processed
    if "_thumbnail" in file:
        continue
    if ext.lower() in [".jpg",".png",".jpeg"]:
        
        with Image.open(infile) as im:
            # TODO figure out the logic of forcing image size
            # w,h=im.size
            # if h != 150:

                
            # im.thumbnail(size)
            new_image= im.resize((150,150))
            new_image.save(file + "_thumbnail.png", "PNG")


