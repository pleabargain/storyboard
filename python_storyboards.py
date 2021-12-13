# !/usr/bin/python3

import PySimpleGUI as sg
import random
import webbrowser

import os

image_list = []

#load the files from the target directory
for root, dirs, files in os.walk("/home/dgd/Desktop/python.storyboard.flashcards/random.images"):
   for name in files:
      print(os.path.join(root, name))
      image_list.append(os.path.join(root, name))
#    for name in dirs:
#       print(os.path.join(root, name))




sg.ChangeLookAndFeel('GreenTan')

# ------ Menu Definition ------ #
menu_def = [['&File', ['&Open', '&Save', 'E&xit', 'Properties']],
            ['&Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
            ['&Help', '&Open_docs'], ]

# ------ Column Definition ------ #
column1 = [[sg.Text('Column 1', background_color='lightblue', justification='center', size=(10, 1))],
           [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 1',key = "Spin1",enable_events=True)],
           [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2')],
           [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3')]]

# the vocab will go here
# # vocabulary_column = [sg.Multiline(default_text='This is the default Text should you decide not to type anything', size=(35, 3)),
#      sg.Multiline(default_text='A second multi-line', size=(35, 3))]
# #header Vocabulary

# # image_first_column = [sg.Image(filename="/home/dgd/Desktop/python.storyboard.flashcards/random.images/airport.terminal.png",
#                         key='canvas1'),
#                         sg.Text('\u0394 one!', size=(5, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],

# # image_second_column = [sg.Image(filename="/home/dgd/Desktop/python.storyboard.flashcards/random.images/airport.terminal.png",
#                         key='canvas2'),
#                         [sg.Text('\u0394 two!', size=(5, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)]

# # image_third_column = [sg.Image(filename="/home/dgd/Desktop/python.storyboard.flashcards/random.images/airport.terminal.png",
#                         key='canvas3'),
#                         sg.Text('\u0394 three', size=(5, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)]



layout = [
    #TODO column with image and text 
    [sg.Menu(menu_def, tearoff=True)],
    # [sg.Canvas(size=(500, 200), key='canvas')],
    #TODO use image resizer on images
    [sg.Image(filename="/home/dgd/Desktop/python.storyboard.flashcards/random.images/airport.terminal.png",
                        key='canvas1'),
    sg.Image(filename="/home/dgd/Desktop/python.storyboard.flashcards/random.images/airport.terminal.png",
                        key='canvas2'),
    sg.Image(filename="/home/dgd/Desktop/python.storyboard.flashcards/random.images/airport.terminal.png",
                        key='canvas3')],
                
    [sg.Text('\u0394 one!', size=(5, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE),
    sg.Text('\u0394 two!', size=(5, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE),
    sg.Text('\u0394 three', size=(5, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
    
    #create button
    [sg.Button("change image",key="canvas_button1")],

    [sg.Text('\u0394(Almost) All widgets in one Window!', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
    [sg.Text('Here is some text.... and a place to enter text')],
    [sg.InputText('This is my text')],
    [sg.Frame(layout=[
    [sg.Checkbox('Checkbox', size=(10,1)),  sg.Checkbox('My second checkbox!', default=True)],
    [sg.Radio('My first Radio!     ', "RADIO1", default=True, size=(10,1)), sg.Radio('My second Radio!', "RADIO1")]], title='Options',title_color='red', relief=sg.RELIEF_SUNKEN, tooltip='Use these to set flags')],
    [sg.Multiline(default_text='This is the default Text should you decide not to type anything', size=(35, 3)),
     sg.Multiline(default_text='A second multi-line', size=(35, 3))],
    [sg.InputCombo(('Combobox 1', 'Combobox 2'), size=(20, 1)),
     sg.Slider(range=(1, 100), orientation='h', size=(34, 20), default_value=85)],
    [sg.InputOptionMenu(('Menu Option 1', 'Menu Option 2', 'Menu Option 3'))],
    [sg.Listbox(values=('Listbox 1', 'Listbox 2', 'Listbox 3'), size=(30, 3)),
     sg.Frame('Labelled Group',[[
     sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=25, tick_interval=25),
     sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=75),
     sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=10),
     sg.Column(column1, background_color='lightblue')]])],
    [sg.Text('_' * 80)],
    [sg.Text('Choose A Folder', size=(35, 1))],
    [sg.Text('Your Folder', size=(15, 1), auto_size_text=False, justification='right'),
     sg.InputText('Default Folder'), sg.FolderBrowse()],
    [sg.Submit(tooltip='Click to submit this form'), sg.Cancel()]]

window = sg.Window('Everything is awesome', 
                    
                    layout, 
                    size = (800,600),
                    location=(2100, 2000),
                    default_element_size=(40, 1), 
                    grab_anywhere=False)

while True:


    event, values = window.read()



    if event == "Open_docs":
        webbrowser.open("https://pysimplegui.readthedocs.io/en/latest/",new=1,autoraise=True )
        # pass

    if event == "canvas_button1":
        random.shuffle(image_list)
        window["canvas1"].update(filename=image_list[0])
        window["canvas2"].update(filename=image_list[1])
        window["canvas3"].update(filename=image_list[2])
        

    if event == "Spin1":
        sg.PopupOK("spin 1 click")
        # pass    

    if event == "Exit" or event == "Cancel":
        break
    



window.close()

# sg.Popup('Title',
#          'The results of the window.',
#          'The button clicked was "{}"'.format(event),
#          'The values are', values)