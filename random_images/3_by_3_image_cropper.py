from PIL import Image # import pillow library (can install with "pip install pillow")

#3 X 3 grid
# 1 2   3 
# 4 5 6  
# 7 8 9 

# 1

source = "/home/dgd/Desktop/python_storyboard_flashcards/random_images/3x3.adjectives.04c79bd94d0610469a5599e0618e486f.jpg"
final = "/home/dgd/Desktop/python_storyboard_flashcards/random_images/"
im = Image.open(source)
# (left, upper, right, lower)
im = im.crop( (1, 40, 190, 230) ) # 
im.save(final + '1card.png') # saves the image

# 4
im = Image.open(source)
# x,y,bottom right,bottom left
im = im.crop( (0, 230, 190, 420) ) # 
im.save(final + '2card.png') # saves the image

# # 7
im = Image.open(source)
# x,y,bottom right,bottom left
im = im.crop( (0, 420, 190, 630) ) # 
im.save(final + '7card.png') # saves the image


# # 1 2   3 
# # 4 5 6  
# # 7 8 9 

# #2 
im = Image.open(source)
# (left, upper, right, lower)
im = im.crop( (190, 40, 380, 250) ) # 
im.save(final + '2card.png') # saves the image


# # 5
im = Image.open(source)
# (left, upper, right, lower)
im = im.crop( (190, 250, 380, 430) ) # 
im.save(final + '5card.png') # saves the image

# # 8
im = Image.open(source)
# (left, upper, right, lower)
im = im.crop( (190, 450, 380, 630) ) # 
im.save(final + '8card.png') # saves the image



# # 1 2   3 
# # 4 5 6  
# # 7 8 9 


# # 3
im = Image.open(source)
# (left, upper, right, lower)
im = im.crop( (380, 40, 580, 240) ) # 
im.save(final + '3card.png') # saves the image


# # 6
im = Image.open(source)
# (left, upper, right, lower)
im = im.crop( (380, 240, 580, 440) ) # 
im.save(final + '6card.png') # saves the image

# # 9
im = Image.open(source)
# (left, upper, right, lower)
im = im.crop( (380, 440, 580, 640) ) # 
im.save(final + '9card.png') # saves the image

