# !/usr/bin/python3

import PySimpleGUI as sg
import random
import webbrowser

import os
import os.path

from PySimpleGUI.PySimpleGUI import WIN_CLOSED, Exit, button_color_to_tuple

#TODO add vocabulary column
#TODO set text file to open code and local file
#done set default image size to 150x150
#done load only images with thumbnail in the name
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


verbs_list = []
nouns_list = []
adjectives_list =[]



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

def read_list_from_file():
    verbs_list.clear()
    nouns_list.clear()
    adjectives_list.clear()
    with open("verbs.txt") as myfile:
        for line in myfile.readlines():
            verbs_list.append(line.strip())
    with open("nouns.txt") as myfile:
        for line in myfile.readlines():
            nouns_list.append(line.strip())
    with open("adjectives.txt") as myfile:
        for line in myfile.readlines():
            adjectives_list.append(line.strip())




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

#call the function
read_list_from_file()
# print(verbs_list)

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

left_tab= sg.Tab ("adj noun reg verb", [
    [sg.Text("verb",size=(17,1)),sg.Text("adj",size=(17,1)),sg.Text("noun",size=(17,1)),],
    [   sg.Listbox(verbs_list,key="verbs_list_box",enable_events=True,change_submits=True,size=(15,15)),
        sg.Listbox(adjectives_list,key="adjectives_list_box",enable_events=True,change_submits=True,size=(15,15)),
        sg.Listbox(nouns_list,key="nouns_list_box",enable_events=True,change_submits=True,size=(15,15)),
        
        sg.Button("reload"),sg.Button("randomize"),
    
    ],
    

    ])

right_tab= sg.Tab ("tenses tab", [
        #create button
    [sg.Button("shuffle the images",
                key = "image_shuffle",
                ),
    # sg.Button("easy"),
    # sg.Button("intermediate"),
    # sg.Button("hard"),
    # sg.Button("elite"),
    sg.Button("comparatives"),
    sg.Button("idioms"),
    sg.Button("prepositional phrases"),
    sg.Button("conditionals")

                ],


    [column_left, column_center,column_right],

    ])


layout = [
    
    #TODO column with image and text 
    [sg.Menu(menu_def, tearoff=True)],
    # [sg.Canvas(size=(500, 200), key='canvas')],
    #TODO use image resizer on images
    
    [sg.TabGroup([[left_tab,right_tab]],key="tabgroup")],
    
    # three images start here


    # #create button
    # [sg.Button("shuffle the images",
    #             key = "image_shuffle",
    #             ),
    #  sg.Button("easy"),
    #  sg.Button("intermediate"),
    #  sg.Button("hard"),
    #  sg.Button("elite"),

    #             ],


    # [column_left, column_center,column_right],
    
]
    


window = sg.Window('Development! Learn English with Dennis', 
                    
                    layout, 
                    background_color="lightblue",
                    size = (900,600),
                    location=(2000, 1700),
                    default_element_size=(35, 1), 
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
        
# button in left tab
    if event == 'reload':
        read_list_from_file()
        window["verbs_list_box"].update(values=verbs_list)
        window["nouns_list_box"].update(values=nouns_list)
        window["adjectives_list_box"].update(values=adjectives_list)

# button in left tab
    if event == 'randomize':
        window["verbs_list_box"].update(set_to_index=random.randint(0,len(verbs_list)-1))
        window["nouns_list_box"].update(set_to_index=random.randint(0,len(nouns_list)-1))
        window["adjectives_list_box"].update(set_to_index=random.randint(0,len(adjectives_list)-1))
        # (set_to_index=random.randint(0,len(verbs_list)-1))




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

    
    if event == "comparatives":
        webbrowser.open("https://docs.google.com/spreadsheets/d/150r972lV3ogmCmlmpjkHNOoX6tIO26Gd4EYzdfCGUW4/edit?usp=sharing",new=1,autoraise=True )

    if event == "idioms":
        webbrowser.open("https://docs.google.com/spreadsheets/d/15u8oWVJNmjvfkOOvF696E1o-Tz6lBZkr7ctJ6CBLYVk/edit?usp=sharing",new=1,autoraise=True )


    if event == "prepositional phrases":
        webbrowser.open("https://docs.google.com/spreadsheets/d/1R3rYYL7H7wC86Z8HeNFy_QzCvqXJSv6w8tKb3wsM30E/edit?usp=sharing",new=1,autoraise=True )

    if event == "conditionals":
        webbrowser.open("https://docs.google.com/spreadsheets/d/1VKcLMETbyEnWpVEeXc5j5NjEa_UF0ydMBInS-ljoWhs/edit?usp=sharing",new=1,autoraise=True )





    if event == sg.WIN_CLOSED or event == "Cancel" or event == 'Exit' :
        break


    # if event == "Exit" or event == "Cancel":
    #     break
    



window.close()

# sg.Popup('Title',
#          'The results of the window.',
#          'The button clicked was "{}"'.format(event),
#          'The values are', values)