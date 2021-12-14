# !/usr/bin/python3


import PIL
import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont

import os

from resizeimage import resizeimage

img_folder = '/home/dgd/Desktop/python.storyboard.flashcards/verb.images'

fileext = '.jpg' + '.png'
suffix = '_RESIZED'

for img_filename in os.listdir(img_folder):
    filename, ext = os.path.splitext(img_filename)

    if ext == fileext:
        print(filename, ext)
        src_img_filepath = os.path.join(img_folder, img_filename)
        dst_img_filepath = os.path.join(img_folder, filename+suffix, ext)

        with Image.open(src_img_filepath) as image:
            cover = resizeimage.resize_cover(image, [200, 100])
            cover.save(dst_img_filepath, image.format)