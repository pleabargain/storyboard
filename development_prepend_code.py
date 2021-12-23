# try with regext
# resource: 
# https://www.geeksforgeeks.org/how-to-search-and-replace-text-in-a-file-in-python/
# Importing re module

# script should read a directory 
# parse SVG files
# open the SVG files
# find and replace a certain string
# save the file with a new name 
# e.g. old_SVG_name_NEW.svg 

# save old_SVG_name_NEW.svg as .png 
# e.g. old_SVG_name_NEW_thumbnail.png

# final png should be approximately 150 pixel 



import re

# importing os module
import os
 
# giving directory name
folderdir = '/home/dgd/Desktop/python_storyboard_flashcards/random_images/'
 
# giving file extensions
ext = ('.svg')
 
# iterating over directory and subdirectory to get desired result
for path, dirc, files in os.walk(folderdir):
    for name in files:
        if name.endswith(ext):
            print(name)  # printing file name

# now I need to figure out how to store this list and pass the list to the processing loop


  
# Creating a variable and storing
# the text that we want to search
search_text = "^<svg"
  
#Creating a variable and storing
# the text that we want to update
replace_text = """<svg width="150px" height="150px" """


# # Creating a function to
# # replace the text
def replacetext(search_text,replace_text):
  
    # Opening the file in read and write mode
    with open('/home/dgd/Desktop/python_storyboard_flashcards/random_images/a_bikini.svg','r+') as f:
  
        # Reading the file data and store
        # it in a file variable
        file = f.read()
          
        # Replacing the pattern with the string
        # in the file data
        file = re.sub(search_text, replace_text, file)
  
        # Setting the position to the top
        # of the page to insert data
        f.seek(0)
          
        # Writing replaced data in the file
        f.write(file)
  
        # Truncating the file size
        f.truncate()
  
    # Return "Text replaced" string
    return "Text replaced"
  
# # Creating a variable and storing
# # the text that we want to search
# search_text = "^<svg"
  
# #Creating a variable and storing
# # the text that we want to update
# replace_text = """<svg width="150px" height="150px" """










##############
# Calling the replacetext function
# and printing the returned statement
# resource 
# https://stackoverflow.com/questions/4454298/prepend-a-line-to-an-existing-file-in-python

#this works
# with open('//home/dgd/Desktop/python_storyboard_flashcards/test_prepend_problem.md', 'r') as original: data = original.read()
# with open('/home/dgd/Desktop/python_storyboard_flashcards/test_prepend_problem'+'_test'+'.md', 'w') as modified: modified.write("new first line\n" + data)

# but it won't work with my problem because I need to find and replace text
# print(replacetext(search_text,replace_text))