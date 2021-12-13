# !/usr/bin/python3

import PySimpleGUI as sg
import random
import webbrowser

import os
import os.path

from PySimpleGUI.PySimpleGUI import button_color_to_tuple

image_list = []

# past_simple
# past_continuous
# past_perfect_continuous
# past_perfect
# present_simple
# present_continuous
# present_perfect_continuous
# present_perfect
# future_simple
# future_continuous
# future_perfect_continuous
# future_perfect


def reset_tenses():
    """
    clear the background color
    """
    window["past_simple"].update(background_color = "lightblue")
    window["past_continuous"].update(background_color = "lightblue")
    window["past_perfect_continuous"].update(background_color = "lightblue")
    window["past_perfect"].update(background_color = "lightblue")
    window["present_simple"].update(background_color = "lightblue")
    window["present_continuous"].update(background_color = "lightblue")
    window["present_perfect_continuous"].update(background_color = "lightblue")
    window["present_perfect"].update(background_color = "lightblue")
    window["future_simple"].update(background_color = "lightblue")
    window["future_continuous"].update(background_color = "lightblue")
    window["future_perfect_continuous"].update(background_color = "lightblue")
    window["future_perfect"].update(background_color = "lightblue")



def split_filename(original_filename):

    """
    This will split a file name by _ so that a space will appear
    returns a string minus the file extension
    display only the text after the last slash

    """
    #strip the last four chars from the text
    text = os.path.split(original_filename)[1]
    text = text[:-4]
    return text.replace("_", " ")



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
# column1 = [[sg.Text('Column 1', background_color='lightblue', justification='center', size=(10, 1))],
#            [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 1',key = "Spin1",enable_events=True)],
#            [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2')],
#            [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3')]]

# the vocab will go here
vocabulary_column = [sg.Multiline(default_text='This is the default Text should you decide not to type anything', size=(35, 3)),
     sg.Multiline(default_text='A second multi-line', size=(35, 3))]
#header Vocabulary

column_left = sg.Column([
                            #header
                            [sg.Text("past simple",key="past_simple")],
                            [sg.Text("past continuous",key="past_continuous")],
                            [sg.Text("past perfect",key="past_perfect")],
                            [sg.Text("past perfect continuous",key="past_perfect_continuous")],
                            [sg.Multiline('\u0394 one!', 
                            key= "text1a",
                            size=(15,1), 
                            justification='center', 
                            font=("Helvetica", 15)) 
                            ],

                            [sg.Image(filename="",
                            key='canvas1a')
                            ],
                            
                            [sg.Multiline('\u0394 one!', 
                            key= "text1b",size=(15,1), 
                            justification='center', 
                            font=("Helvetica", 15)), 
                            ],

                        
                            [sg.Image(filename="",
                            key='canvas1b'),]
                        ])

column_center = sg.Column([
                            #header
                            [sg.Text("present simple",key="present_simple")],
                            [sg.Text("present continuous",key="present_continuous")],
                            [sg.Text("present perfect",key="present_perfect")],
                            [sg.Text("present perfect continuous",key="present_perfect_continuous")],

                            [sg.Multiline('\u0394 one!', 
                            key= "text2a",
                            size=(15,1), 
                            justification='center', 
                            font=("Helvetica", 15)) 
                            ],

                            [sg.Image(filename="",
                            key='canvas2a')
                            ],
                            
                            [sg.Multiline('\u0394 one!', 
                            key= "text2b",size=(15,1), 
                            justification='center', 
                            font=("Helvetica", 15)), 
                            ],

                        
                            [sg.Image(filename="",
                            key='canvas2b'),]

                            ])

column_right = sg.Column([ #header
                            [sg.Text("future simple",key="future_simple")],
                            [sg.Text("future continuous",key="future_continuous")],
                            [sg.Text("future perfect",key="future_perfect")],
                            [sg.Text("future perfect continuous",key="future_perfect_continuous")],
                            [sg.Multiline('\u0394 one!', 
                            key= "text3a",
                            size=(15,1), 
                            justification='center', 
                            font=("Helvetica", 15)) 
                            ],

                            [sg.Image(filename="",
                            key='canvas3a')
                            ],
                            
                            [sg.Multiline('\u0394 one!', 
                            key= "text3b",
                            size=(15,1), 
                            justification='center', 
                            font=("Helvetica", 15)), 
                            ],

                        
                            [sg.Image(filename="",
                            key='canvas3b'),]
                        ])



layout = [
    #TODO column with image and text 
    [sg.Menu(menu_def, tearoff=True)],
    # [sg.Canvas(size=(500, 200), key='canvas')],
    #TODO use image resizer on images
    # three images start here

    [column_left, column_center,column_right],
    
    #create button
    [sg.Button("shuffle the images",
                key = "image_shuffle",
                ),
     sg.Button("easy"),
     sg.Button("medium"),
     sg.Button("hard"),
     sg.Button("elite"),

                ],
]
    


window = sg.Window('Everything is awesome', 
                    
                    layout, 
                    background_color="lightblue",
                    size = (800,720),
                    location=(2100, 1900),
                    default_element_size=(40, 1), 
                    grab_anywhere=True)

while True:


    event, values = window.read()


    if event == "Open_docs":
        webbrowser.open("https://pysimplegui.readthedocs.io/en/latest/",new=1,autoraise=True )
        # pass

    if event == "image_shuffle":
        random.shuffle(image_list)
        window["canvas1a"].update(filename=image_list[0])
        window["canvas1b"].update(filename=image_list[1])
        window["canvas2a"].update(filename=image_list[2])
        window["canvas2b"].update(filename=image_list[3])
        window["canvas3a"].update(filename=image_list[4])
        window["canvas3b"].update(filename=image_list[5])
        window["text1a"].update(split_filename(image_list[0]))
        window["text1b"].update(split_filename(image_list[1]))
        window["text2a"].update(split_filename(image_list[2]))
        window["text2b"].update(split_filename(image_list[3]))
        window["text3a"].update(split_filename(image_list[4]))
        window["text3b"].update(split_filename(image_list[5]))
        
    if event == 'easy':
        reset_tenses()
        window["past_simple"].update(background_color = 'red')
        window["present_simple"].update(background_color = 'red')
        window["future_simple"].update(background_color = 'red')



    if event == 'medium':
        reset_tenses()
        window[random.choice(["past_simple","past_continuous"])].update(background_color = 'red')
        window[random.choice(["present_simple","present_continuous"])].update(background_color = 'red')
        window[random.choice(["future_simple","future_continuous"])].update(background_color = 'red')
        
    if event == 'hard':
        reset_tenses()
        window[random.choice(["past_simple","past_continuous", "past_perfect"])].update(background_color = 'red')
    
    if event == 'elite':
        reset_tenses()
        window[random.choice(["past_simple",
                            "past_continuous", 
                            "past_perfect", 
                            "past_perfect_continuous"])
                            ].update(background_color = 'red')
    

        

    if event == "Exit" or event == "Cancel":
        break
    



window.close()

# sg.Popup('Title',
#          'The results of the window.',
#          'The button clicked was "{}"'.format(event),
#          'The values are', values)