from PIL import ImageFont, ImageDraw, Image

with open("/home/dgd/Desktop/python_storyboard_flashcards/idea_grammar_tracker_tab/common_errors.md") as myfile:
    lines=myfile.readlines()



image = Image.open('/home/dgd/Desktop/python_storyboard_flashcards/background.jpg')
draw = ImageDraw.Draw(image)
txt = "Hello Horst! Here is some text!"
fontsize = 1  # starting font size

W, H = image.size

# portion of image width you want text width to be
blank = Image.new('RGB',(150, 150))


font = ImageFont.truetype("/home/dgd/Desktop/python_storyboard_flashcards/SourceCodePro-VariableFont_wght.ttf", fontsize)
print (image.size)
print (blank.size)

while (font.getsize(txt)[0] < blank.size[0]) and (font.getsize(txt)[1] < blank.size[1]):
    # iterate until the text size is just larger than the criteria
    fontsize += 1
    font = ImageFont.truetype("/home/dgd/Desktop/python_storyboard_flashcards/SourceCodePro-VariableFont_wght.ttf", fontsize)

# # optionally de-increment to be sure it is less than criteria
# fontsize -= 1
# font = ImageFont.truetype("/usr/share/fonts/truetype/customfonts/KeepCalm-Medium.ttf", fontsize)

w, h = draw.textsize(txt, font=font)

print ('final font size',fontsize)
draw.text(((W-w)/2,(H-h)/2), txt, font=font, fill="black") # put the text on the image
image.save('new_sample-out.png') # save it