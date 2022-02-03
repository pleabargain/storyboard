from PIL import Image # import pillow library (can install with "pip install pillow")

#3 X 4 grid
# 1 2   3  4
# 5 6   7  8
# 9 10  11 12

# 1
im = Image.open('/home/dgd/Desktop/02a8c02e87121cd218886edb3d775cdc.jpg')
# (left, upper, right, lower)
im = im.crop( (1, 0, 146, 230) ) # 
im.save('/home/dgd/Desktop/1card.png') # saves the image

# 5
im = Image.open('/home/dgd/Desktop/02a8c02e87121cd218886edb3d775cdc.jpg')
# x,y,bottom right,bottom left
im = im.crop( (0, 220, 155, 400) ) # 
im.save('/home/dgd/Desktop/5card.png') # saves the image

# 9
im = Image.open('/home/dgd/Desktop/02a8c02e87121cd218886edb3d775cdc.jpg')
# x,y,bottom right,bottom left
im = im.crop( (0, #left edge
                400,#good 
                160,# bottom right 
                590) 
                ) # 
im.save('/home/dgd/Desktop/9card.png') # saves the image


#2 
im = Image.open('/home/dgd/Desktop/02a8c02e87121cd218886edb3d775cdc.jpg')
im = im.crop( (150, 0, 280, 230) ) # 
im.save('/home/dgd/Desktop/2card.png') # saves the image


# 6
# 0,0 upper left corner
# 0,0 bottom right corner
im = Image.open('/home/dgd/Desktop/02a8c02e87121cd218886edb3d775cdc.jpg')
# x,y x,y
im = im.crop( (150, 220, 290, 400) ) # 
im.save('/home/dgd/Desktop/6card.png') # saves the image

# 10
# 0,0 upper left corner
# 0,0 bottom right corner
im = Image.open('/home/dgd/Desktop/02a8c02e87121cd218886edb3d775cdc.jpg')
# x,y x,y
im = im.crop( (150, 400, 290, 570) ) # 
im.save('/home/dgd/Desktop/10card.png') # saves the image





# 3
im = Image.open('/home/dgd/Desktop/02a8c02e87121cd218886edb3d775cdc.jpg')
# x,y,bottom right,bottom left
im = im.crop( (280, 0, 420, 230) ) # 
im.save('/home/dgd/Desktop/3card.png') # saves the image


# 7
im = Image.open('/home/dgd/Desktop/02a8c02e87121cd218886edb3d775cdc.jpg')
# x,y,bottom right,bottom left
# 120, 140
im = im.crop( (280, 220, 420, 400) ) # 
im.save('/home/dgd/Desktop/7card.png') # saves the image

# 11
im = Image.open('/home/dgd/Desktop/02a8c02e87121cd218886edb3d775cdc.jpg')
# x,y,bottom right,bottom left
im = im.crop( (280,410, 420, 570) ) # 
im.save('/home/dgd/Desktop/11card.png') # saves the image





# 4
im = Image.open('/home/dgd/Desktop/02a8c02e87121cd218886edb3d775cdc.jpg')
# x,y,bottom right,bottom left
im = im.crop( (410, 0, 560, 230) ) # 
im.save('/home/dgd/Desktop/4card.png') # saves the image

# 8
im = Image.open('/home/dgd/Desktop/02a8c02e87121cd218886edb3d775cdc.jpg')
# x,y,bottom right,bottom left
im = im.crop( (410, 220, 560, 400) ) # 
im.save('/home/dgd/Desktop/8card.png') # saves the image

# 12
im = Image.open('/home/dgd/Desktop/02a8c02e87121cd218886edb3d775cdc.jpg')
# x,y,bottom right,bottom left
im = im.crop( (410, 410, 560, 570) ) # 
im.save('/home/dgd/Desktop/12card.png') # saves the image














# im.show() # opens the image