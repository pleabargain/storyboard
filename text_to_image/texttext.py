# source
# https://www.haptik.ai/tech/putting-text-on-images-using-python-part2/




# /usr/share/fonts/truetype/malayalam/AnjaliOldLipi-Regular.ttf

###
# goal  
# open text file 
# read in line by line of text

# render each line as an image 
# with words fitting inside the image
###


from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
 
with open("/home/dgd/Desktop/python_storyboard_flashcards/text_to_image/words_for_list.txt") as myfile:
    #top scope
    lines=myfile.readlines()
    print(lines)


def text_wrap(text, font, max_width):
    # inside function local scope
    lines = []
    # If the width of the text is smaller than image width
    # we don't need to split it, just add it to the lines array
    # and return
    if font.getsize(text)[0] <= max_width:
        lines.append(text)
    else:
        # split the line by spaces to get words
        words = text.split(' ')  
        i = 0
        # append every word to a line while its width is shorter than image width
        while i < len(words):
            line = ''        
            while i < len(words) and font.getsize(line + words[i])[0] <= max_width:                
                line = line + words[i] + " "
                i += 1
            if not line:
                line = words[i]
                i += 1
            # when the line gets longer than the max width do not append the word,
            # add the line to the lines array
            lines.append(line)    
    return lines
 
 
def draw_text(text):    
    # open the background file
    img = Image.open('/home/dgd/Desktop/python_storyboard_flashcards/text_to_image/background.png')
    draw = ImageDraw.Draw(img)    
    # size() returns a tuple of (width, height)
    image_size = img.size
 
    # create the ImageFont instance
    font_file_path = '/usr/share/fonts/truetype/malayalam/AnjaliOldLipi-Regular.ttf'
    font = ImageFont.truetype(font_file_path, size=50, encoding="unic")
 
    # get shorter lines
    # call text_wrap function
    lines = text_wrap(text, font, image_size[0])
    print("after text wrap")
    print (lines) # ['This could be a single line text ', 'but its too long to fit in one. ']
    # need to write each file out with unique correctly formatted name
    # with underscores between the words
    # img.save('newsample-out.png') # save it

       
    line_height = font.getsize('hg')[1]
    
    x = 10
    y = 20
    for line in lines:
        # draw the line on the image
        draw.text((x, y), line, font=font, fill=(0, 0, 0))
        
        # update the y position so that we can use it for next line
        y = y + line_height
    # save the image
    img.save('word2.png', optimize=True)
 
if __name__ == "__main__":
    draw_text("This could be a single line text but its too long to fit in one.")
    # how do I get the output of the a
    # draw_text(lines)