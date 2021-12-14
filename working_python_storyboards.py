# !/usr/bin/python3

import PySimpleGUI as sg
import random
import webbrowser

import os
import os.path

from PySimpleGUI.PySimpleGUI import button_color_to_tuple

image_list = []

#list of tenses
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
    clear the background color of the text objects
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
for root, dirs, files in os.walk("/home/dgd/Desktop/python_storyboard_flashcards/random_images"):
   for name in files:
      print(os.path.join(root, name))
      image_list.append(os.path.join(root, name))
#    for name in dirs:
#       print(os.path.join(root, name))


# set the theme color
sg.ChangeLookAndFeel('GreenTan')

# ------ Menu Definition ------ #
menu_def = [['&File', ['&Open', '&Save', 'E&xit', 'Properties']],
            ['&Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
            ['&Help', 'help','&Open_docs'], ]

# ------ Column Definition ------ #
# column1 = [[sg.Text('Column 1', background_color='lightblue', justification='center', size=(10, 1))],
#            [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 1',key = "Spin1",enable_events=True)],
#            [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2')],
#            [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3')]]

# the vocab will go here
# vocabulary_column = [sg.Multiline(default_text='This is the default Text should you decide not to type anything', size=(35, 3)),
#      sg.Multiline(default_text='A second multi-line', size=(35, 3))]
#header Vocabulary

# column_vocab = sg.Column([
#                         sg.Multiline(default_text='A second multi-line', size=(5, 5))
#                           ])

column_left = sg.Column([
                            #header
                            [sg.Text("past simple",
                            key="past_simple",
                            
                            tooltip='Past Simple - I built a new garage last month.')],

                            [sg.Text("past continuous",
                            key="past_continuous", 
                            tooltip='Past Continuous - I was building a wall yesterday.')],
                            
                            [sg.Text("past perfect",
                            key="past_perfect",
                            tooltip='Past Perfect - By the time my last company went bust we had already built the new shopping center.')],

                            [sg.Text("past perfect continuous",
                            key="past_perfect_continuous",
                            tooltip= 'Past Perfect Continuous - We had been building the new\n shopping center for 2 months when we heard about the bankruptcy.'
                            )],

                            [sg.Multiline('text', 
                            key= "text1a",
                            size=(17,1), 
                            font=("Helvetica", 12)) 
                            ],

                            [sg.Image(filename="",
                            key='canvas1a')
                            ],
#####################                            
                            [sg.Multiline('text', 
                            key= "text1b",
                            size=(17,1), 
                            font=("Helvetica", 12)), 
                            ],

                        
                            [sg.Image(filename="",
                            key='canvas1b'),]
                        ])

column_center = sg.Column([
                            #header
                            [sg.Text("present simple",
                            key="present_simple",
                            tooltip='Present Simple - I usually build commercial buildings.',
                            )],


                            [sg.Text("present continuous",
                            key="present_continuous",
                            tooltip='Present Continuous - It is Monday morning and I am building a wall.',
                            )],


                            [sg.Text("present perfect",
                            key="present_perfect",
                            tooltip='Present Perfect Simple - I have already built two shopping centers this year.',                            
                            )],


                            [sg.Text("present perfect continuous",
                            key="present_perfect_continuous",
                            tooltip='Present Perfect Continuous - I have been building this shopping centre since we won the contract.'
                            )],

                            [sg.Multiline('\u0394', 
                            key= "text2a",
                            size=(17,1), 
                            font=("Helvetica", 12)) 
                            ],

                            [sg.Image(filename="",
                            key='canvas2a')
                            ],
                            
                            [sg.Multiline('\u0394', 
                            key= "text2b",size=(17,1), 
                            font=("Helvetica", 12)), 
                            ],

                        
                            [sg.Image(filename="",
                            key='canvas2b'),]

                            ])

column_right = sg.Column([ #header
                            [sg.Text("future simple",key="future_simple",
                            tooltip="""Future Simple - I think I'll build my own\n house when I can afford to.""",)],
                            [sg.Text("future continuous",key="future_continuous",
                            tooltip="""Future Continuous - I'm building a new garage tomorrow.""")],
                            
                            [sg.Text("future perfect",key="future_perfect",
                            tooltip="""Future Perfect Simple - I hope I will have already built my \nown house by the time I am 40.""")],
                            
                            [sg.Text("future perfect continuous",key="future_perfect_continuous",
                            tooltip="""Future Perfect Continuous - This time next week I will have\n been building this shopping center for two months.""")],

                            [sg.Multiline('\u0394', 
                            key= "text3a",
                            size=(17,1), 
                            font=("Helvetica", 12)) 
                            ],

                            [sg.Image(filename="",
                            key='canvas3a')
                            ],
                            
                            [sg.Multiline('\u0394', 
                            key= "text3b",
                            size=(17,1), 
                            font=("Helvetica", 12)), 
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
    


window = sg.Window('Learn English with Dennis', 
                    
                    layout, 
                    background_color="lightblue",
                    size = (900,720),
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
        window[random.choice(["past_simple","past_continuous"])].update(background_color = 'white')
        window[random.choice(["present_simple","present_continuous"])].update(background_color = 'white')
        window[random.choice(["future_simple","future_continuous"])].update(background_color = 'white')



    if event == 'medium':
        reset_tenses()
        window[random.choice(["past_simple","past_continuous",])].update(background_color = 'white')
        window[random.choice(["present_simple","present_perfect","present_continuous",])].update(background_color = 'white')
        window[random.choice(["future_simple","future_continuous",])].update(background_color = 'white')
        
    if event == 'hard':
        reset_tenses()
        window[random.choice(["past_simple",   "past_continuous",  "past_perfect","past_perfect_continuous",]) ].update(background_color = 'white')
        window[random.choice(["present_simple",   "present_continuous",   "present_perfect",]) ].update(background_color = 'white')
        window[random.choice(["future_simple",   "future_continuous",  "future_perfect",]) ].update(background_color = 'white')
    
    if event == 'elite':
        reset_tenses()
        window[random.choice(["past_simple",   "past_continuous",  "past_perfect", "past_perfect_continuous"])].update(background_color = 'white')
        window[random.choice(["present_simple",   "present_continuous","present_perfect_continuous",  "present_perfect",]) ].update(background_color = 'white')
        window[random.choice(["future_simple",   "future_continuous",  "future_perfect","future_perfect_continuous"]) ].update(background_color = 'white')
    
    # if event == 'help':
    #     sg.popup_notify("Some text",location = (900,900))

        

    if event == "Exit" or event == "Cancel":
        break
    



window.close()

# sg.Popup('Title',
#          'The results of the window.',
#          'The button clicked was "{}"'.format(event),
#          'The values are', values)