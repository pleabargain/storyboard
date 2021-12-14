# !/usr/bin/python3
import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont

import os

path = "/home/dgd/Desktop/python_storyboard_flashcards/verb_images"
dirs = os.listdir(path)

def resize():
    for item in dirs:
        if item == '.jpg':
            continue
        if os.path.isfile(path+item):
            image = Image.open(path+item)
            file_path, extension = os.path.splitext(path+item)
            size = image.size

            new_image_height = 190
            new_image_width = int(size[1] / size[0] * new_image_height)

            image = image.resize((new_image_height, new_image_width), Image.ANTIALIAS)
            image.save(file_path + "_small" + extension, 'JPEG', quality=90)


resize()