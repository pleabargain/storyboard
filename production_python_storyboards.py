# !/usr/bin/python3

import PySimpleGUI as sg
import random
import webbrowser

import os
import os.path

from PySimpleGUI.PySimpleGUI import WIN_CLOSED, Exit, button_color_to_tuple

#TODO add vocabulary column
#TODO set default image size to 150x150
#TODO load only images with thumbnail in the name
image_list = []


# irregular_list = []
# adjectives_describing_things= []
# adjectives_describing_people= []
# noun= []
# linking_words= []
# modals= []




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
#TODO finish stripping prefixes
    """
    This will split a file name by _ so that a space will appear
    returns a string minus the file extension
    display only the text after the last slash

    """
    #DENNIS! complex words must be first eg. noun_animal_ BEFORE noun
    list_of_unwanted_words = ["noun_animal_",
                                "noun_food_",
                                "noun_clothing_",
                                "noun_insect_",
                                "noun_",
                                "verb_"]

    #strip the last four chars from the text
    text = os.path.split(original_filename)[1]
    text = text[:-14]
    for unwanted in list_of_unwanted_words:
        if text.startswith(unwanted):
            text=text[len(unwanted):]
            break
    # if text.endswith("_thumbnail")

    return text.replace("_", " ")


# TODO 
# try except to make sure the folder exists
# load the files from the target directory
#TODO load only images with thumbnail in the name
#TODO load only images that are 150x150
for root, dirs, files in os.walk("/home/dgd/Desktop/python_storyboard_flashcards/random_images"):
   for name in files:
       if name.endswith("_thumbnail.png"):
           print(os.path.join(root, name))
           image_list.append(os.path.join(root, name))



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
                            enable_events=True,
                            
                            tooltip='Past Simple - I built a new garage last month.')],

                            [sg.Text("past continuous",
                            key="past_continuous", 
                            enable_events=True,

                            tooltip='Past Continuous - I was building a wall yesterday.')],
                            
                            [sg.Text("past perfect",
                            key="past_perfect",
                            enable_events=True,

                            tooltip='Past Perfect - By the time my last company went bust we had already built the new shopping center.')],

                            [sg.Text("past perfect continuous",
                            key="past_perfect_continuous",
                            enable_events=True,
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
                            enable_events=True,
                            tooltip='Present Simple - I usually build commercial buildings.',
                            )],


                            [sg.Text("present continuous",
                            key="present_continuous",
                            enable_events=True,
                            tooltip='Present Continuous - It is Monday morning and I am building a wall.',
                            )],


                            [sg.Text("present perfect",
                            key="present_perfect",
                            enable_events=True,
                            tooltip='Present Perfect Simple - I have already built two shopping centers this year.',                            
                            )],


                            [sg.Text("present perfect continuous",
                            key="present_perfect_continuous",
                            enable_events=True,
                            tooltip='Present Perfect Continuous - I have been building this shopping centre since we won the contract.'
                            )],

                            [sg.Multiline('\U0001F934', 
                            key= "text2a",
                            size=(17,1), 
                            font=("Helvetica", 12)) 
                            ],

                            # [sg.Text('\U0001F934', 
                            # key= "text2a",
                            # size=(17,1), 
                            # font=("Helvetica", 12)) 
                            # ],

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
                            [sg.Text("future simple",
                            key="future_simple",
                            enable_events=True,
                            tooltip="""Future Simple - I think I'll build my own\n house when I can afford to.""",)],

                            [sg.Text("future continuous",
                            enable_events=True,
                            key="future_continuous",
                            tooltip="""Future Continuous - I'm building a new garage tomorrow.""")],
                            
                            [sg.Text("future perfect",
                            key="future_perfect",
                            enable_events=True,
                            tooltip="""Future Perfect Simple - I hope I will have already built my \nown house by the time I am 40.""")],
                            
                            [sg.Text("future perfect continuous",
                            key="future_perfect_continuous",
                            enable_events=True,
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


    #create button
    [sg.Button("shuffle the images",
                key = "image_shuffle",
                ),
     sg.Button("easy"),
     sg.Button("medium"),
     sg.Button("hard"),
     sg.Button("elite"),

                ],


    [column_left, column_center,column_right],
    
]
    


window = sg.Window('Production! Learn English with Dennis', 
                    
                    layout, 
                    background_color="lightblue",
                    #first number is width
                    size = (1100,620),
                    location=(2000, 1700),

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

#   if event == "edit_encouragement_markdown":
#             window["status"].update("please make edits, save and exit the external editor to continue")
#             window.refresh()
#             os.system("{} {}".format(EXTERNAL_EDITOR, ENCOURAGEMENT_FILE))
#             window["status"].update("ready to build")
    
    # if event == 'help':
    #     sg.popup_notify("Some text",location = (900,900))

    if event == "past_simple":
        webbrowser.open("https://docs.google.com/spreadsheets/d/1NkmOcQcNU8Dirk_rM04yEF5CS9yaSnYGip0Tyq0AkIU/edit?usp=sharing",new=1,autoraise=True )


    if event == "past_continuous":
        webbrowser.open("https://docs.google.com/spreadsheets/d/14FxeIfy6HA1nFK1HA-t301v-7x2Hf4BoYxnu1hKtm1M/edit?usp=sharing",new=1,autoraise=True )

    if event == "past_perfect_continuous":
        webbrowser.open("https://docs.google.com/spreadsheets/d/1eQYZQA9qWQLEjEwwgBv6hupkzLELxVWXwZEukJ2He2I/edit?usp=sharing",new=1,autoraise=True )

    if event == "past_perfect":
        webbrowser.open("https://docs.google.com/spreadsheets/d/1KzJ68cM0VBsthrfsGJRIXCV4MWXcSIcDdDWfH-Gfl3M/edit?usp=sharing",new=1,autoraise=True )

###
    
    if event == "present_simple":
        webbrowser.open("https://docs.google.com/spreadsheets/d/1xv0ZFe6_l66spkXWPyWrzu5k1KPNb3OWKL52Xg71DuE/edit?usp=sharing",new=1,autoraise=True )


    if event == "present_continuous":
        webbrowser.open("https://docs.google.com/spreadsheets/d/1SKgIK56P0qla0l2KEuii35AjPWrg4YJGYqw2prV7BIw/edit?usp=sharing",new=1,autoraise=True )

    if event == "present_perfect_continuous":
        webbrowser.open("https://docs.google.com/spreadsheets/d/1mQoBCdNpjYee6lX5sxwz1oS2xpmkVeimY-CVUnRgxoA/edit?usp=sharing",new=1,autoraise=True )

    if event == "present_perfect":
        webbrowser.open("https://docs.google.com/spreadsheets/d/1vAlXCM5dD8EVvt9W_YYz7ZNN6UZumT0MClnazfF7oGY/edit?usp=sharing",new=1,autoraise=True )


###


    if event == "future_simple":
        webbrowser.open("https://docs.google.com/spreadsheets/d/1ipHIxokBppXG_BXsVZ02J-HbXtzA5xLLPSm6prZlZ2Q/edit?usp=sharing",new=1,autoraise=True )


    if event == "future_continuous":
        webbrowser.open("https://docs.google.com/spreadsheets/d/1ggv9CToDdZBcjTjDF92r5AYOzAzvFhWZSFuraUdT5mE/edit?usp=sharing",new=1,autoraise=True )

    if event == "future_perfect_continuous":
        webbrowser.open("https://docs.google.com/spreadsheets/d/1ePg18VgsvrrIv1JKcuF6KDTak3jQ46A1ALyv4ElHI5U/edit?usp=sharing",new=1,autoraise=True )

    if event == "future_perfect":
        webbrowser.open("https://docs.google.com/spreadsheets/d/1aq_OhW0JRTGNrowS7Q4RCl52cHx7S9Upha7z9VYp-3o/edit?usp=sharing",new=1,autoraise=True )

    



    if event == sg.WIN_CLOSED or event == "Cancel" or event == 'Exit' :
        break


    # if event == "Exit" or event == "Cancel":
    #     break
    



window.close()

# sg.Popup('Title',
#          'The results of the window.',
#          'The button clicked was "{}"'.format(event),
#          'The values are', values)