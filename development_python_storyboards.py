# !/usr/bin/python3

from asyncio import subprocess
from tkinter import CENTER
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import WIN_CLOSED, Exit, button_color_to_tuple

import subprocess
import random
import webbrowser
import datetime

import os
import os.path
import csv
import json
import glob
import pandas as pd
import spacy
from spacy import displacy
from pathlib import Path


# TODO search code for ALL keys and produce a report :goal:normalize naming of keys
# TODO question: possible to call a tab as a function call that way the tabs can be reused easily elsewhere?
# TODO question: What other defaults can I call when starting the application?
# TODO with open text and md files, sort and remove duplicates first.

nlp = spacy.load('en_core_web_sm')

# TODO this needs to be a function call so that it can be reused with better more meaningful names
# I want to reuse this over and over


# this code will NOT run if this file is not available!
with open("/home/dgd/Desktop/python_storyboard_flashcards/idea_grammar_tracker_tab/common_errors.md") as myfile:
    lines=myfile.readlines()
    #TODO error checker to keep file clean
#take first ten lines
#remove \n
top_ten =[line.strip() for line in lines[:10]]
print(top_ten)


# learn about student names in the file
# this code will NOT run if this file is not available!
# TODO sort the names in the output
# TODO alert user if duplicate names
with open("/home/dgd/Desktop/python_storyboard_flashcards/students/student_names.txt") as myfile:
    lines=myfile.readlines()

#strip empty lines
#GLOBALS
root = Path("/home/dgd/Desktop/EnglishHelpsYourCareer/")
DB_FILES = [file for file in root.iterdir() if file.stem.startswith("db_")]
DB_FILES2 = [file.stem for file in DB_FILES]
DB_FILES2.sort()



student_names= [line.strip() for line in lines if len(line.strip())>0]

ERROR_LOG_FILENAME = "/home/dgd/Desktop/python_storyboard_flashcards/error_log/error_log.txt"

DATABASE = "/home/dgd/Desktop/EnglishHelpsYourCareer/question_bank_2.csv"

#this uses pipes as 
INSTRUCTIONS_FILENAME = "/home/dgd/Desktop/EnglishHelpsYourCareer/category_instructions.csv"
#create empty dict
instructions = {}
#read csv 
#category_name	category_instructions

with open(INSTRUCTIONS_FILENAME) as tmp:
        ireader = csv.reader(tmp, delimiter='|', quotechar='"')
        for row in ireader:
            cat, text = row
            instructions[cat] = text


selected_topic =""
FIREFOX = "firefox"
EXTERNAL_EDITOR = "code"  # command to start the external editor to edit markdown files

NEGOTIATION_TEMPLATE = """
prepared {}\n

thank you {}



"""



mermaid_template = """verb: {}\nadjective: {}\nnoun: {}\nquantifier: {}\nsubordinating conjunction: {}\n
#mermaid
Q: 
A:
Q: 
A:

---

"""

# create a dictionary for the grammar tracker
# nested dictionary key = student name value = another dictionary
# dictionary year month day value another dictionary

student_progress = {}

#TODO set text file to open code and local file

#done add vocabulary column: see grammar tracker tab
#done fix negotiation text so that it shows only the randomly selected text list_box doesn't work
#done set default image size to 150x150
#done load only images with thumbnail in the name


# create empty dictionaries to hold the contents of the files
test_gif = "/home/dgd/Pictures/2022_Dounia/2022HappyNewYear.gif"
original_image_list = []
verbs_list = []
nouns_list = []
adjectives_list =[]
quantifiers_list = []
subordinating_conjunctions_list = []

#negotiations
prepare_0_list = []
agenda_01_list = []
making_proposals_02_list = []
suggestions_03_list = []
agreeing_04_list = []
objecting_05_list = []
prioritizing_06_list = []
clarification_07_list = []
compromising_08_list = []
bargaining_09_list = []
postponing_10_list = []
concluding_11_list = []
seal_the_deal_12_list = []


### pros and cons
sum_of_pros= 0
sum_of_cons= 0
pros_cons_issues = []

### question student export field names for export csv
# 

STUDENT_FOLDER = "/home/dgd/Desktop/python_storyboard_flashcards/students"
QUESTION_FOLDER = "/home/dgd/Desktop/python_storyboard_flashcards/question_tab"

attention_field_names =[
                        "timestamp",
                        "UNIQUE_ID",
                        "student_answer1"	,
                        ]


#TODO fix this name
list_of_unwanted_words = [  
                            "adjective_feeling_",
                            "adjective_person_",
                            "adjective_",
                            "daily_routine_",
                            "dentist_",
                            "hard_skills_",
                            
                            "idiom_business_negotiation_",
                            "idiom_business_",
                            "idiom_time_",
                            "idiom_",
                            "jobs_",
                            "medical_terms_illness_",
                            "medical_terms_",
                            "measure_words_",
                            "modals_",
                            "money_",
                            "life_skills_",
                            "noun_animal_",
                            "noun_body_part_",
                            "noun_city_",
                            "noun_clothing_",
                            "noun_medical_terms_",
                            "noun_insect_",
                            "noun_food_countable",
                            "noun_food_uncountable",
                            "noun_food_",
                            "noun_kitchen_",
                            "noun_law_",
                            "noun_travel_",
                            "noun_business_vocabulary_",
                            "noun_transportation_",
                            "noun_",
                            "preposition_",
                            "soft_skills_",
                            "phrase_",
                            "phrasal_verbs_",
                            #"to_get_",
                            "valentines_day",
                            "verb_restaurant_",
                            "verb_past_perfect_",
                            "verb_kitchen_",
                            "verb_travel_",
                            "verb_",
                            "weather_",
                        ]


question_student_field_names =[
                        "timestamp",
                        "student_choice",
                        "UNIQUE_ID",	
                        "CATEGORY",	
                        "QUESTION",	
                        "CORRECT_ANSWERS",	
                        "CHOICE1",
                    	"CHOICE2",
                        "CHOICE3",	
                        "CHOICE4",	
                        "CHOICE5",	
                        "CHOICE6",	    
                        "CHOICE7",	
                        "CHOICE8",	
                        "CHOICE9",	
                        "CHOICE10",

                                ]

def open_clean_save(filename):
    '''
    TODO: add a test to make sure file exists
    if no 
    then post error message to term and keep going
    open file name
    remove duplicates
    sort alpha
    save

    Arguments: takes filename

    returns: ?

    '''
    with open (filename) as myfile:
        lines = myfile.readlines()
    lines = list(set(lines))
    lines.sort()
    with open(filename,"w") as myfile:
        myfile.writelines(lines)


def clear_pros_cons():
    """
    this wil clear the fields in the pro con tab
    """
    window['analysis'].update("")
    for i in range (7):

        window[f'pros_{i}'].update("")
        window[f'slider_pros_{i}'].update(1)
        window[f'cons_{i}'].update("")
        window[f'slider_cons_{i}'].update(1)

def save_attention():

    """
    save attention file
    enter text automatically by clicking on answer
    
    """
    
    if (not values["needs_attention"])  and (values["student_answer1" ]==""):
        return
        

    if values["db_category"] == "":
        sg.PopupError("cat empty",location=(2000,10))
        return
    if values["student_name"] == "":
        sg.PopupError("student name",location=(2000,10))
        return
    
    #create csv
    attention_filename = QUESTION_FOLDER + "/needs_attention.csv"
       #check to see if file exists
    
    csv_exists= os.path.exists(attention_filename)
        
   
    with open (attention_filename,'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=attention_field_names)
        if not csv_exists:
            writer.writeheader()
        #this will get all of the object attributes
        # sg.PopupOK(dir(window["db_question_number"]))


        # sg.PopupOK(window["db_question_number"].DisplayText)
        data_dict = {
                    "timestamp":  "{}.{}.{} {}:{}:{}".format(datetime.date.today().year, 
                    datetime.date.today().month,
                    datetime.date.today().day,
                    datetime.datetime.today().hour,
                    datetime.datetime.today().minute,
                    datetime.datetime.today().second,
                    ),
                    "UNIQUE_ID":window["db_question_number"].DisplayText,
                    "student_answer1":	values["student_answer1"],
                    }

    
        #create student_name + questions.csv  append 
        writer.writerow(data_dict)    



def save_student_answers():
    """
    student says x to a question
   
    """
    
    if values["db_category"] == "":
        sg.PopupError("cat empty",location=(2000,10))
        return
    if values["student_name"] == "":
        sg.PopupError("student name",location=(2000,10))
        return
    
    #create csv
    student_question_filename = STUDENT_FOLDER + "/" +values["student_name"]+".csv"
    #check to see if file exists
    
    csv_exists= os.path.exists(student_question_filename)
        
   
    with open (student_question_filename,'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=question_student_field_names)
        if not csv_exists:
            writer.writeheader()
        #this will get all of the object attributes
        # sg.PopupOK(dir(window["db_question_number"]))


        # sg.PopupOK(window["db_question_number"].DisplayText)
        data_dict = {
                            "timestamp":  "{}.{}.{} {}:{}:{}".format(datetime.date.today().year, 
                            datetime.date.today().month,
                            datetime.date.today().day,
                            datetime.datetime.today().hour,
                            datetime.datetime.today().minute,
                            datetime.datetime.today().second,
                            ),
                        "student_choice": values["student_question_choice"],
                        "UNIQUE_ID":window["db_question_number"].DisplayText,	
                        "CATEGORY":values["db_category"],	
                        #multiline
                        "QUESTION":values["db_question"],	
                        "CORRECT_ANSWERS":window["correct_answer"].DisplayText,	
                        "CHOICE1":window["db_choice1"].DisplayText,
                    	"CHOICE2":window["db_choice2"].DisplayText,
                        "CHOICE3":window["db_choice3"].DisplayText,	
                        "CHOICE4":window["db_choice4"].DisplayText,	
                        "CHOICE5":window["db_choice5"].DisplayText,	
                        # "CHOICE6":window["db_choice6"].DisplayText,	    
                        # "CHOICE7":window["db_choice7"].DisplayText,	
                        # "CHOICE8":window["db_choice8"].DisplayText,	
                        # "CHOICE9":window["db_choice9"].DisplayText,	
                        # "CHOICE10":window["db_choice10"].DisplayText,
                        }

    
        #create student_name + questions.csv  append 
        writer.writerow(data_dict)    



def get_categorylist(database):
    """
    opens csv with pandas dataframe
    """
    try:
        df = pd.read_csv(database)
    except Exception as e:
        sg.PopupError("error with reading database:" + e, keep_on_top=True)
        return
    unique_cat_list = [topic for topic in df['CATEGORY'].unique() if
                       (type(topic) == str) and (topic is not None) and (len(topic) > 0) and (topic != "nan")]
    # sg.PopupOK(unique_cat_list)
    for field in df:
        print(field)


    unique_cat_list.sort()
    return unique_cat_list, df

# all_categories = get_categorylist(DATABASE)
#load the file from the database and dataframe
category_list,df = get_categorylist(DATABASE)
df2 = None
print(category_list)



# TODO
# save pros cons csv to pro con folder!
# TODO 
# get all linking words into one big block 
# create function that calls it and randomizes the output
# use on pros and cons
###
# TODO
# use linking words in negotiation tab

def open_generic_file(file,key):
        with open(file) as myfile:
            lines = myfile.readlines()
        selected_topic = random.choice(lines).strip()
        window[key].update(selected_topic)



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
    This function is primarily used in the storyboard tenses tab
    """
    #DENNIS! complex words must be first eg. noun_animal_ BEFORE noun
    # image name prefixes

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
    #TODO refactor this mess
    verbs_list.clear()
    nouns_list.clear()
    adjectives_list.clear()
    quantifiers_list.clear()
    subordinating_conjunctions_list.clear()
    # negotiations
    prepare_0_list.clear()      
    agenda_01_list.clear()
    making_proposals_02_list.clear()
    suggestions_03_list.clear()
    agreeing_04_list.clear()
    objecting_05_list.clear()
    prioritizing_06_list.clear()
    clarification_07_list.clear()
    compromising_08_list.clear()
    bargaining_09_list.clear()
    postponing_10_list.clear()
    concluding_11_list.clear()
    seal_the_deal_12_list.clear()
    # pros and cons
    pros_cons_issues.clear()
    
    
 
###tenses
    open_clean_save("word_lists/quantifiers.md")
    with open("word_lists/verbs.md") as myfile:
        for line in myfile.readlines():
            verbs_list.append(line.strip())

    open_clean_save("/home/dgd/Desktop/python_storyboard_flashcards/word_lists/nouns.md")
    with open("/home/dgd/Desktop/python_storyboard_flashcards/word_lists/nouns.md") as myfile:
        for line in myfile.readlines():
            nouns_list.append(line.strip())

    open_clean_save("word_lists/adjectives.md")
    with open("word_lists/adjectives.md") as myfile:
        for line in myfile.readlines():
            adjectives_list.append(line.strip())
    

    open_clean_save("word_lists/quantifiers.md")
    with open("word_lists/quantifiers.md") as myfile:
        #function call clean up the file
        for line in myfile.readlines():
            quantifiers_list.append(line.strip())


    open_clean_save("word_lists/list_subordinating_conjunctions.md")
    with open("word_lists/list_subordinating_conjunctions.md") as myfile:
        for line in myfile.readlines():
            subordinating_conjunctions_list.append(line.strip())


###start negotiations
    with open("negotiations_tab/prepare_0.md") as myfile:
        for line in myfile.readlines():
            prepare_0_list.append(line.strip())

    
    with open("negotiations_tab/agenda_01.md") as myfile:
        for line in myfile.readlines():
            agenda_01_list.append(line.strip())

    
    with open("negotiations_tab/making_proposals_02.md") as myfile:
        for line in myfile.readlines():
            making_proposals_02_list.append(line.strip())

    
    with open("negotiations_tab/suggestions_03.md") as myfile:
        for line in myfile.readlines():
            suggestions_03_list.append(line.strip())

    
    with open("negotiations_tab/agreeing_04.md") as myfile:
        for line in myfile.readlines():
            agreeing_04_list.append(line.strip())

    
    with open("negotiations_tab/objecting_05.md") as myfile:
        for line in myfile.readlines():
            objecting_05_list.append(line.strip())

    
    with open("negotiations_tab/prioritizing_06.md") as myfile:
        for line in myfile.readlines():
            prioritizing_06_list.append(line.strip())

    
    with open("negotiations_tab/clarification_07.md") as myfile:
        for line in myfile.readlines():
            clarification_07_list.append(line.strip())

    
    with open("negotiations_tab/compromising_08.md") as myfile:
        for line in myfile.readlines():
            compromising_08_list.append(line.strip())

    
    with open("negotiations_tab/bargaining_09.md") as myfile:
        for line in myfile.readlines():
            bargaining_09_list.append(line.strip())

    
    with open("negotiations_tab/postponing_10.md") as myfile:
        for line in myfile.readlines():
            postponing_10_list.append(line.strip())

    
    with open("negotiations_tab/concluding_11.md") as myfile:
        for line in myfile.readlines():
            concluding_11_list.append(line.strip())

    
    with open("negotiations_tab/seal_the_deal_12.md") as myfile:
        for line in myfile.readlines():
            seal_the_deal_12_list.append(line.strip())
### start pros and cons
    with open("pros_cons_tab/pros_cons_events.md") as myfile:
        for line in myfile.readlines():
            seal_the_deal_12_list.append(line.strip())


# TODO 
# TODO try except to make sure the folder exists
# TODO load the files from the target directory
# TODO load only images with thumbnail in the name


#why doesn't this print an error?
try:
    for root, dirs, files in os.walk("/home/dgd/Desktop/python_storyboard_flashcards/random_images"):
        for name in files:
            if name.endswith("_thumbnail.png"):
                #  print(os.path.join(root, name))
                # append all files with thumbnail in the name
                original_image_list.append(os.path.join(root, name))
except:
    print("folder not found")



# for root, dirs, files in os.walk("/home/dgd/Desktop/python_storyboard_flashcards/random_images"):
#    for name in files:
#        if name.endswith("_thumbnail.png"):
#         #  print(os.path.join(root, name))
#            image_list.append(os.path.join(root, name))

#call the function
read_list_from_file()
# print(verbs_list)

# set the theme color
sg.ChangeLookAndFeel('GreenTan')

# ------ Menu Definition ------ #
menu_def = [['&File', ['&Open', '&Save', 'E&xit', 'Properties']],
            ['&Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
            ['&Vocabulary',
                ['core vocab',
                '2 letter words',
                '3 letter words',
                '4 letter words',
                'business vocab'
                ],
            ],

            ['&Pronunciation',
                ['pron_ed_id',
                'pron_ed_t',
                'pron_soft_d',
                'silent_b',
                'pron_k',
                'silent_s',
                'misc_pronunciation',
                
                ],
            ],


            ['&Linking Words',
                [
                'M_addition',
                'M_comparison',
                'M_concession',
                'M_condition',
                'M_contrast',
                'M_emphasis',
                'M_illustration',
                'M_reason',
                'M_results',# test note
                'M_subordinating',
                "M_summarizing",
                "M_coordinating",
                ],

            ],
            ['&Resources',
                ['rhyme_site',
                ]
            ],
            ['&Help', 
                ['tips',
                'README',
            ],
            '&Open_docs'], 
            ]

#TODO add business vocabulary

timeline_column_one = sg.Column([
                                [sg.Button("change time",
                                font = ("helvetica", 12),
                                size = (18,1),
                                tooltip="click to change all of the times")], 




                                [sg.Text("\u0394 time changes",
                                font = ("helvetica", 12),
                                justification = "left",
                                key="past1",
                                size = (30,1),
                                enable_events=True,
                                tooltip='Past events1')],

###
                                [sg.Text("\u0394 time changes",
                                font = ("helvetica", 12),
                                justification = "left",
                                key="past2",
                                size = (None,None),
                                enable_events=True,
                                tooltip='Past events2')], 
###
                                [sg.Text("\u0394 time changes",
                                font = ("helvetica", 12),
                                justification = "left",
                                key="past3",
                                size = (None,None),
                                enable_events=True,
                                tooltip='past3 column one')],

                                [sg.Text("\u0394 time changes",
                                font = ("helvetica", 12),
                                justification = "left",
                                key="past4",
                                size = (30,1),
                                enable_events=True,
                                tooltip='past time 4 column one')],
###
                                [sg.Text("\u0394 time changes",
                                font = ("helvetica", 12),
                                justification = "left",
                                key="present1",
                                size = (30,1),
                                enable_events=True,
                                tooltip='present1')],

                                [sg.Text("\u0394 time changes",
                                font = ("helvetica", 12),
                                justification = "left",
                                key="present2",
                                size = (30,1),
                                enable_events=True,
                                tooltip='present1')],

                                [sg.Text("\u0394 time changes",
                                font = ("helvetica", 12),
                                justification = "left",
                                key="present3",
                                size = (30,1),
                                enable_events=True,
                                tooltip='present1')],

                                [sg.Text("\u0394 time changes",
                                font = ("helvetica", 12),
                                justification = "left",
                                key="now_event",
                                size = (30,1),
                                enable_events=True,
                                tooltip='Now is a great time!')],
###
                                [sg.Text("\u0394 time changes",
                                key="future1",
                                font = ("helvetica", 12),
                                justification = "left",
                                size = (30,1),
                                enable_events=True,
                                tooltip='future1 event')],
###
                                [sg.Text("\u0394 time changes",
                                key="future2",
                                font = ("helvetica", 12),
                                justification = "left",
                                size = (30,1),
                                enable_events=True,
                                tooltip='future2 event')],
###
                                [sg.Text("\u0394 time changes",
                                key="future3",
                                font = ("helvetica", 12),
                                justification = "left",
                                size = (30,1),
                                enable_events=True,
                                tooltip='future3 event')],

                                [sg.Text("\u0394 time changes",
                                key="future4",
                                font = ("helvetica", 12),
                                justification = "left",
                                size = (30,1),
                                enable_events=True,
                                tooltip='future4 event')],


                                ])



timeline_column_two = sg.Column([
                                
                                [sg.Button("randomize timeline events",
                                font = ("helvetica", 12),
                                size = (20,1),
                                        )
                                ],


                                [sg.Text("timeline column one",
                                key="event1",
                                font = ("helvetica", 12),
                                justification = "left",
                                size = (30,2),
                                enable_events=True,
                                tooltip='This is a random event. line 452')],


                                [sg.Text("past2 column one",
                                key="event2",
                                font = ("helvetica", 12),
                                justification = "left",
                                size = (30,2),
                                enable_events=True,
                                tooltip='line 461')], 

                                [sg.Text("eventpast3",
                                key="event3",
                                font = ("helvetica", 12),
                                justification = "left",
                                size = (30,2),
                                enable_events=True,
                                tooltip='line 469')],

                                [sg.Text("now column one",
                                key="event4",
                                font = ("helvetica", 12),
                                justification = "left",
                                size = (30,2),
                                enable_events=True,
                                tooltip='line 477')],

                                [sg.Text("timeline column one",
                                key="event5",
                                font = ("helvetica", 12),
                                justification = "left",
                                size = (30,2),
                                enable_events=True,
                                tooltip='line 485')],

                                [sg.Text("event 6 timeline column one",
                                key="event6",
                                font = ("helvetica", 12),
                                justification = "left",
                                size = (30,2),
                                enable_events=True,
                                tooltip='line 493')],

                                [sg.Text("timeline column one",
                                key="event7",
                                font = ("helvetica", 12),
                                justification = "left",
                                size = (30,2),
                                enable_events=True,
                                tooltip='line 501')],

                                ])


timeline_column_three = sg.Column([
                                [sg.Button("randomize adverbs",
                                font = ("helvetica",12),
                                button_color="blue",
                                size = (30,1),
                                )
                                ],
                                
                                [sg.Text("timeline column one",
                                key="adverb1",
                                font = ("helvetica", 12),

                                size = (30,2),
                                enable_events=True,
                                tooltip='key adverb1 of time'),
                                ],

###
                                [sg.Text("past2 column one",
                                key="adverb2",
                                font = ("helvetica", 12),
                                size = (30,2),
                                enable_events=True,
                                tooltip='This is a tool tip for adverb2')], 
###
                                [sg.Text("eventpast3",
                                key="adverb3",
                                size = (30,2),
                                font = ("helvetica", 12),
                                enable_events=True,
                                tooltip='This is a tool tip timeline column one')],
###
                                [sg.Text("now column one",
                                key="adverb4",
                                size = (30,2),
                                font = ("helvetica", 12),
                                enable_events=True,
                                tooltip='This is a tool tip timeline column one')],
###
                                [sg.Text("timeline column one",
                                key="adverb5",
                                size = (30,2),
                                font = ("helvetica", 12),
                                enable_events=True,
                                tooltip='This is a tool tip for adverb5')],
###
                                [sg.Text("timeline column one",
                                key="adverb6",
                                size = (30,2),
                                font = ("helvetica", 12),
                                enable_events=True,
                                tooltip='This is a tool tip for adverb6')],
###
                                [sg.Text("timeline column one",
                                key="adverb7",
                                size = (30,2),
                                font = ("helvetica", 12),
                                enable_events=True,
                                tooltip='This is a tool tip for adverb7')],

                                ])


timeline_column_four = sg.Column([
                                ###
                                 [sg.Button("place holder",
                                 size = (15,1),
                                 font = ("helvetica", 12),
                                                              
                                 )],           

                                [sg.Text("past simple",
                                key="past_simple1",
                                size = (30,1),
                                font = ("helvetica", 12),
                                enable_events=True,
                                tooltip='Past Simple - I built a new garage last month.')],

                                [sg.Text("past continuous",
                                                                size = (30,1),
                                font = ("helvetica", 12),

                                key="past_continuous", 
                                enable_events=True,
                                tooltip='Past Continuous - I was building a wall yesterday.')],
                               
                                 [sg.Text("past perfect",
                                key="past_perfect",
                                size = (30,1),
                                font = ("helvetica", 12),

                                enable_events=True,
                                tooltip='Past Perfect - By the time my last company went bust we had already built the new shopping center.')],

                                [sg.Text("past perfect continuous",
                                key="past_perfect_continuous",
                                size = (30,1),
                                font = ("helvetica", 12),

                                enable_events=True,
                                tooltip= 'Past Perfect Continuous - We had been building the new\n shopping center for 2 months when we heard about the bankruptcy.'
                                )],

                                [sg.Text("present simple",
                                key="present_simple",
                                size = (30,1),
                                font = ("helvetica", 12),


                                enable_events=True,
                                tooltip='Present Simple - I usually build commercial buildings.',
                                )],


                            [sg.Text("present continuous",
                            key="present_continuous",
                            size = (30,1),
                            font = ("helvetica", 12),
                            enable_events=True,
                            tooltip='Present Continuous - It is Monday morning and I am building a wall.',
                            )],


                            [sg.Text("present perfect",
                            key="present_perfect",
                            size = (30,1),
                            font = ("helvetica", 12),                            
                            enable_events=True,
                            tooltip='Present Perfect Simple - I have already built two shopping centers this year.',                            
                            )],


                            [sg.Text("present perfect continuous",
                            key="present_perfect_continuous",
                            size = (30,1),
                            font = ("helvetica", 12),                            
                            enable_events=True,
                            tooltip='Present Perfect Continuous - I have been building this shopping centre since we won the contract.'
                            )],

                            [sg.Text("future simple",
                            key="future_simple",
                            size = (30,1),
                            font = ("helvetica", 12),
                            
                            enable_events=True,
                            tooltip="""Future Simple - I think I'll build my own\n house when I can afford to.""",)],

                            [sg.Text("future continuous",
                            enable_events=True,
                            key="future_continuous",
                            size = (30,1),
                            font = ("helvetica", 12),
                            
                            tooltip="""Future Continuous - I'm building a new garage tomorrow.""")],
                            
                            [sg.Text("future perfect",
                            key="future_perfect",
                            size = (30,1),
                            font = ("helvetica", 12),
                            
                            enable_events=True,
                            tooltip="""Future Perfect Simple - I hope I will have already built my \nown house by the time I am 40.""")],
                            
                            [sg.Text("future perfect continuous",
                            key="future_perfect_continuous",
                            size = (30,1),
                            font = ("helvetica", 12),
                            
                            enable_events=True,
                            tooltip="""Future Perfect Continuous - This time next week I will have\n been building this shopping center for two months.""")],
                                                              

                                ])




bingo_column = sg.Column(
    [
        [sg.Text("challenge",
                key="bingo1_button",
                tooltip= "key challenge: TODO\nsort this list!",
                enable_events=True,
                font = ("helvetica",16)

                ),

        sg.Combo(values=DB_FILES2,
                    key="bingo1",
                    tooltip ="key bingo1",
                    enable_events=True,
                    font = ("helvetica",16),
                ),
                                                                
        ],


        [sg.Multiline("",
                    key="bingo_text1",
                    size = (50,5),
                    font = ("helvetica",16),
                    disabled = True,
                    justification="center",
                    enable_events=True,
                    )
        ],

        [sg.Text("bingo2",
                key="bingo2_button",
                tooltip= "key challenge: TODO\nsort this list!",
                enable_events=True,
                font = ("helvetica",16),
                ),
                
        
        sg.Combo(values=DB_FILES2,
                key="bingo2",
                font = ("helvetica",16),
                enable_events=True,             
                )
        ],

        [sg.Multiline("",
                    key="bingo_text2",
                    size = (50,5),
                    font = ("helvetica",16),
                    enable_events=True,
                    )
        ]

    ])



tenses_tab_column_left = sg.Column(
                            [
                                                  
                            
                            [sg.Multiline('text', 
                            key= "text1a",
                            justification = "center",
                            size=(15,2), 
                            font=("Helvetica", 16)) 
                            ],

                            [sg.Image(filename="",
                            # no easy way to center the images
                            # justification = "center",
                            key='canvas1a')
                            ],
                   
                            [sg.Multiline('text', 
                            key= "text1b",
                            justification = "center",
                            size=(15,2),
                            font=("Helvetica", 16)), 
                            ],

                        
                            [sg.Image(filename="",
                            key='canvas1b'),]
                            ])

tenses_tab_column_center = sg.Column([
                                                       

                            [sg.Multiline('\U0001F934', #guy face emoji
                            key= "text2a",
                            justification = "center",
                            size=(15,2), 
                            font=("Helvetica", 16)) 
                            ],

                           

                            [sg.Image(filename="",
                            key='canvas2a',
                            tooltip = "canvas2a",
                                    )
                            ],
                            
                            [sg.Multiline('\u0394', #delta symbol
                            key= "text2b",
                            tooltip="key text2b",
                            size=(15,2), 
                            justification = "center",
                            font=("Helvetica", 16)), 
                            ],

                        
                            [sg.Image(filename="",
                            key='canvas2b'),]

                            ])

tenses_tab_column_right = sg.Column([ #header
                            
                            [sg.Multiline('\u0394', 
                            key= "text3a",
                            justification = "center",
                            size=(15,2), 
                            font=("Helvetica", 16)) 
                            ],

                            [sg.Image(filename="",
                            key='canvas3a')
                            ],
                            
                            [sg.Multiline('\u0394', 
                            key= "text3b",
                            justification = "center",
                            size=(15,2), 
                            font=("Helvetica", 16)), 
                            ],

                        
                            [sg.Image(filename="",
                            key='canvas3b'),]
                        ]
                        
                        
                        )


# NEGOTIATION columns
negotiation_column_left = sg.Column(
                            [
                                                     
                            
                            [sg.Text('0', 
                            justification = "left",
                            tooltip = "prepare line 1074",
                            size=(None,None), 
                            font=("Helvetica", 14)) 
                            ],

                            [sg.Text('1', 
                            justification = "left",
                            tooltip = "agenda line 1081",
                            size=(None,None), 
                            font=("Helvetica", 14)) 
                            ],

                            [sg.Text('2', 
                            justification = "left",
                            tooltip = "offers and proposals line 1088",
                            size=(None,None), 
                            font=("Helvetica", 14)) 
                            ],
                            

                            [sg.Text('3', 
                            justification = "left",
                            tooltip = "suggestions 1096",
                            size=(None,None), 
                            font=("Helvetica", 14)) 
                            ],
                            
                            [sg.Text('4', 
                            justification = "left",
                            tooltip = "agreeing 1103",
                            size=(None,None), 
                            font=("Helvetica", 14)) 
                            ],
                            
                            [sg.Text('5', 
                            justification = "center",
                            tooltip = "objecting line 1110",
                            size=(None,None), 
                            font=("Helvetica", 14)) 
                            ],
                            
                            [sg.Text('6', 
                            justification = "center",
                            tooltip = "prioritizing 1117",
                            size=(None,None), 
                            font=("Helvetica", 14)) 
                            ],
                            
                            [sg.Text('7', 
                            justification = "center",
                            tooltip = "clarifying 1124",
                            size=(None,None), 
                            font=("Helvetica", 14)) 
                            ],
                            
                            [sg.Text('8', 
                            justification = "center",
                            tooltip = "compromising 1131",
                            size=(None,None), 
                            font=("Helvetica", 14)) 
                            ],
                            
                            [sg.Text('9', 
                            justification = "left",
                            tooltip = "bargaining 1138",
                            size=(None,None), 
                            font=("Helvetica", 14)) 
                            ],
                            
                            [sg.Text('10', 
                            justification = "left",
                            tooltip = "postponing 1145",
                            size=(None,None), 
                            font=("Helvetica", 14)) 
                            ],
                            
                           [sg.Text('11', 
                            justification = "left",
                            tooltip = "concluding 1152",
                            size=(None,None), 
                            font=("Helvetica", 14)) 
                            ],
                            
                            [sg.Text('12', 
                            justification = "left",
                            tooltip = "seal the deal 1159",
                            size=(None,None), 
                            font=("Helvetica", 14)) 
                            ],

                        
                        ])

negotiation_column_center = sg.Column([
                            #header
                            
                            [sg.Multiline('prepare', #guy face emoji
                            key="prepare_0_list_box",
                            enable_events=True,
                            autoscroll=True,
                            # justification = "center",
                            size=(60,1), 
                            font=("Helvetica", 14)) ,
                            sg.Button("text",
                                        key="prepare0",)
                            ], 

                            [sg.Multiline('agenda',
                            key="agenda_01_list_box",
                            enable_events=True,
                            # justification = "center",
                            size=(60,1), 
                            font=("Helvetica", 14)) ,
                            sg.Button("text",
                                        key="agenda1",)
                            ],
                            
                            [sg.Multiline('make proposals', #guy face emoji
                            key="making_proposals_02_list_box",
                            enable_events=True,
                            # tooltips = "making_proposals_02_list_box",
                            size=(60,1), 
                            font=("Helvetica", 14)),
                            sg.Button("text",
                                        key="proposals2",)
                             
                            ],
                            
                            [sg.Multiline('make suggestions', #guy face emoji
                            key="suggestions_03_list_box",
                            tooltip = "suggestions_03_list_box",
                            enable_events=True,
                            size=(60,1), 
                            font=("Helvetica", 14)),
                            sg.Button("text",
                                        key="suggestions3",)
                            ],

                            [sg.Multiline('find agreement', 
                            key="agreeing_04_list_box",
                            enable_events=True,
                            size=(60,1), 
                            font=("Helvetica", 14)),
                            sg.Button("text",
                                        key="agreeing4",)
                            ],

                            [sg.Multiline('objecting', 
                            key="objecting_05_list_box",
                            tooltip = "1210",
                            enable_events=True,
                            size=(60,1), 
                            font=("Helvetica", 14)),
                            sg.Button("text",
                                        key="objecting5",)
                            ],

                            [sg.Multiline('prioritizing', 
                            key="prioritizing_06_list_box",
                            tooltip = "1220",
                            enable_events=True,
                            size=(60,1), 
                            font=("Helvetica", 14)),
                               sg.Button("text",
                                        key="prioritizing6",)
                            ],

                            [sg.Multiline('clarifying',
                            key="clarification_07_list_box",
                            tooltip = "1241",
                            enable_events=True,
                            size=(60,1), 
                            font=("Helvetica", 14)),
                                   sg.Button("text",
                                        key="clarification7",)
                            ],

                            [sg.Multiline('compromising', 
                            key="compromising_08_list_box",
                            tooltip ="1237",
                            enable_events=True,
                            size=(60,1), 
                            font=("Helvetica", 14)),
                                   sg.Button("text",
                                        key="compromising8",)
                            ],

                            [sg.Multiline('bargaining', #guy face emoji
                            key="bargaining_09_list_box",
                            enable_events=True,
                            size=(60,1), 
                            font=("Helvetica", 14)),
                                   sg.Button("text",
                                        key="bargaining9",)
                            ],


                            [sg.Multiline('postponing', #guy face emoji
                            key="postponing_10_list_box",
                            tooltip="1271",
                            enable_events=True,
                            size=(60,1), 
                            font=("Helvetica", 14)),
                                   sg.Button("text",
                                        key="postponing10",)
                            ],


                            [sg.Multiline('concluding', 
                            key="concluding_11_list_box",
                            enable_events=True,
                            size=(60,1), 
                            font=("Helvetica", 14)),
                                   sg.Button("text",
                                        key="concluding11",)
                            ],

                            
                            [sg.Multiline('seal the deal', 
                            key="seal_the_deal_12_list_box",
                            enable_events=True,
                            size=(60,1), 
                            tooltip = "1294",
                            font=("Helvetica", 14)),
                                   sg.Button("text",
                                        key="seal_the_deal12",)
                            ],

                        

                            ])

negotiation_column_right = sg.Column([ #header
                            
                            [sg.Button('edit prepare_0'),],
                            [sg.Button('edit agenda_01'),],
                            [sg.Button('edit making_proposals_02'),],
                            [sg.Button('edit suggestions_03'),],
                            [sg.Button('edit agreeing_04'),],
                            [sg.Button('edit objecting_05'),],

                            [sg.Button('edit prioritizing_06'),],
                            [sg.Button('edit clarification_07'),],
                            [sg.Button('edit compromising_08'),],
                            [sg.Button('edit bargaining_09'),],
                            [sg.Button('edit postponing_10'),],
                            [sg.Button('edit concluding_11'),],     
                            [sg.Button('edit seal_the_deal_12')],
                                    ])








tab_one= sg.Tab ("adj noun reg verb", [
    #trying to get random text to display here
    [
    sg.Button("edit verbs list",tooltip="click to edit verbs"),
    sg.Button("edit adjectives list",tooltip="click to edit adjectives"),
    sg.Button("edit nouns list",tooltip="open editor to edit nouns"),
    sg.Button("edit quantifiers list",tooltip="open editor to edit quantifiers"),
    
    sg.Button("edit basic question words",tooltip="line 883 open local editor to edit basic questions")
    ],

    [
    sg.Text("verb",size=(17,1), tooltip = "Verbs are action words."),
    sg.Text("adj",size=(17,1)),
    sg.Text("noun",size=(17,1)),
    sg.Text("quantifiers",size=(17,1)),
    sg.Text("subordinating conjunctions",size=(None,None)),
    ],

        [  # sg.Text(verbs_list,key="verbs_list_box",enable_events=True,size=(15,15)),
            sg.Listbox(verbs_list,key="verbs_list_box",enable_events=True,change_submits=True,size=(15,15)),
            sg.Listbox(adjectives_list,key="adjectives_list_box",enable_events=True,change_submits=True,size=(15,15)),
            sg.Listbox(nouns_list,key="nouns_list_box",enable_events=True,change_submits=True,size=(15,15)),
            sg.Listbox(quantifiers_list,key="quantifiers_list_box",enable_events=True,change_submits=True,size=(15,15)),
            sg.Listbox(subordinating_conjunctions_list,key="subordinating_conjunctions_list_box",enable_events=True,change_submits=True,size=(15,15)),

        ],
            [sg.Multiline(key="simple_sentence_builder_output",
                        size =(70,10), 
                        font = ("helvetica",16),
                        default_text= mermaid_template,   
                        tooltip="simple_sentence_builder_output line 904"), ],
            [sg.Button("reload"),sg.Button("randomize",tooltip="click to randomize"),],
            [sg.Button("save your created sentence",tooltip="save your work to a text file"),],
        
        ],
    

    )

storyboard_tenses_tab_two= sg.Tab ("storyboard tenses tab", [
        #create button
        [sg.Button("shuffle the images",
                    key = "image_shuffle",
                    tooltip = "key image_shuffle",
                    ),

        
        
        
        sg.Text("image filter"), 
        sg.Combo(values=list_of_unwanted_words,
                key = "combo_image_filter", 
                enable_events=True,
                tooltip = "combo_image_filter"),
        sg.Text("filter results: "),
        sg.Text("?",size = (5,1),
                    key = "image_filter_result_number"),
        # #/home/dgd/Pictures/2022_Dounia/2022HappyNewYear.gif
        # sg.Image("/home/dgd/Pictures/2022_Dounia/2022HappyNewYear.gif", key="test_gif"),
        # # window.Element('_IMAGE_').UpdateAnimation(gif103,  time_between_frames=50)
        
        ],


    [tenses_tab_column_left, tenses_tab_column_center,tenses_tab_column_right, bingo_column],

    ])


# ----------------- get negotiation columns


new_negotiation_tab= sg.Tab ("negotiations", [
        #create button
        [sg.Button("idioms1",
                    tooltip = "line 1406",),
        sg.Button("prepositional phrases1",
                   tooltip = "line 1408", ),
        sg.Button("phrasal verbs1",
                   tooltip = "line 1410" ,),
        sg.Button("collocations1",
                    tooltip = "line 1467",)    ,
        # "https://docs.google.com/spreadsheets/d/1zz38JZhW-ZQ-fj35s14UMiFcWbHehc5CpKe2zIUHDUI/edit?usp=sharing"
        sg.Button("conditionals1"),
        sg.Button("comparatives and superlatives1"),
        sg.Button("modals1"),
        sg.Button("question modals_1"),
        ],


    [negotiation_column_left, negotiation_column_center,negotiation_column_right],
    
    [sg.Button('save negotiation text', 
                key =  "save_negotiation_text_to_md",
                size=(85,1),
                tooltip = "key save_negotiation_text_to_md"
                
                 ),
    ],

    ])





#### negotiation TAB
#TODO add edit button so I can quickly go in and add entries

# negotiation_tab_three = sg.Tab("negotiation",
# [
        
# [
#     sg.Text("prepare_0", tooltip="948"),
#     sg.Text(
#             text= "Have you prepared enough?!",
#             # key="prepare_0_list_box",
#             # enable_events=True,
#             font=("Helvetica",14),
#             justification = "center",
#             size=(55,1)
#             ),
#     sg.Button('edit prepare_0'),

# ],

# [
#     sg.Text("agenda_01"),
#     sg.Text(
#             text= "Have you prepared enough?!",
#             key="agenda_01_list_box",
#             enable_events=True,
#            font=("Helvetica", 14),
#             justification = "center",
#             size=(55,1)
#             ),
#     # sg.Button('edit agenda_01'),

# ],

# [
#     sg.Text("making_proposals_02"),
#     sg.Text(
#             text= "Have you prepared enough?!",
#             key="making_proposals_02_list_box",
#             enable_events=True,
#             font=("Helvetica"),
#             justification = "left",
#             size=(None,None)
#             ),
#     # sg.Button('edit making_proposals_02'),

# ],

# [
#     sg.Text("suggestions_03"),
#     sg.Text(
#             text= "Have you prepared enough?!",
#             key="suggestions_03_list_box",
#             enable_events=True,
#             font=("Helvetica"),
#             justification = "left",
#             size=(None,None)
#             ),
#     # sg.Button('edit suggestions_03'),

# ],

# [
#     sg.Text("agreeing_04"),
#     sg.Text(
#             text= "Have you prepared enough?!",
#             key="agreeing_04_list_box",
#             enable_events=True,
#             font=("Helvetica"),
#             justification = "left",
#             size=(None,None)
#             ),
#     # sg.Button('edit agreeing_04'),

# ],

# [
#     sg.Text("objecting_05"),
#     sg.Text(
#             text= "Have you prepared enough?!",
#             key="objecting_05_list_box",
#             enable_events=True,
#             font=("Helvetica"),
#             justification = "left",
#             size=(None,None)
#             ),
#     # sg.Button('edit objecting_05'),

# ],

# [
#     sg.Text("prioritizing_06"),
#     sg.Text(
#             text= "Have you prepared enough?!",
#             key="prioritizing_06_list_box",
#             enable_events=True,
#             font=("Helvetica"),
#             justification = "left",
#             size=(None,None)
#             ),
#     # sg.Button('edit prioritizing_06'),

# ],

# [
#     sg.Text("clarification_07"),
#     sg.Text(
#             text= "Have you prepared enough?!",
#             key="clarification_07_list_box",
#             enable_events=True,
#             font=("Helvetica"),
#             justification = "left",
#             size=(None,None)
#             ),
#     # sg.Button('edit clarification_07'),

# ],

# [
#     sg.Text("compromising_08"),
#     sg.Text(
#             text= "Have you prepared enough?!",
#             key="compromising_08_list_box",
#             enable_events=True,
#             font=("Helvetica"),
#             justification = "left",
#             size=(None,None)
#             ),
#     sg.Text("Connecting Words for Concession", 
#             key="connecting_words_concession",
#             enable_events=True,
#             size= (None,None),
#             ),
#     # sg.Button('edit compromising_08'),

# ],

# [
#     sg.Text("bargaining_09"),
#     sg.Text(
#             text= "Have you prepared enough?!",
#             key="bargaining_09_list_box",
#             enable_events=True,
#             font=("Helvetica"),
#             justification = "left",
#             size=(None,None)
#             ),
#     sg.Text("Linking Words for Condition", 
#             key="linking_words_condition",
#             enable_events=True,
#             size= (None,None),
#             ),

#     # sg.Button('edit bargaining_09'),

# ],

# [
#     sg.Text("postponing_10"),
#     sg.Text(
#             text= "Have you prepared enough?!",
#             key="postponing_10_list_box",
#             enable_events=True,
#             font=("Helvetica"),
#             justification = "left",
#             size=(None,None)
#             ),
#     # sg.Button('edit postponing_10'),

# ],

# [
#     sg.Text("concluding_11"),
#     sg.Text(
#             text= "Have you prepared enough?!",
#             key="concluding_11_list_box",
#             enable_events=True,
#             font=("Helvetica"),
#             justification = "left",
#             size=(None,None)
#             ),
#      sg.Text("Linking Words for Results", 
#                 key="linking_words_results2",
#                 tooltip="bug link not working need to number the keys.line 1323 ",
#                 enable_events=True,
#                 size= (None,None),
#                 ),

#     sg.Text("Summarizing", 
#                 key="connecting_words_summary1",
#                 enable_events=True,
#                 size= (None,None),
#                 ),
#     # sg.Button('edit concluding_11'),

# ],

# [
#     sg.Text("seal_the_deal_12"),
#     sg.Text(
#             text= "Have you prepared enough?!",
#             key="seal_the_deal_12_list_box",
#             enable_events=True,
#             font=("Helvetica"),
#             justification = "left",
#             size=(None,None)
#             ),
#     # sg.Button('edit seal_the_deal_12'),


# ],
# #TODO save the output!


# ###
    
# ]


# )

####################################
timeline_tab= sg.Tab ("timeline tenses tab", 
    [
      
        #create button
        [sg.Button("edit timeline events"), sg.Button("edit adverbs"),sg.Button("place holder"),  ],
    
        [timeline_column_four,timeline_column_one,timeline_column_two, timeline_column_three, ],
    
    ] 
                     )
####################
### pros_cons_tab

pros_cons_tab= sg.Tab ("pros cons", 
        #create button
        [
            #TODO this TEXT object should be a roll down or similar
        [sg.Text("pros and cons issues",size=(None,None),
                key="pros_cons_issues",
                tooltip = "key pros_cons_issues Click to change this item.",
                enable_events=True,
                font=("helvetica",20)),
                sg.Button("edit pros cons issues",
                tooltip="click to open editor"),
                sg.Button("new topic",
                tooltip="line 1718"),
                sg.Button("clear fields",
                tooltip="1720"   ),
                sg.Button("soft skills list",
                tooltip="line 1746"),

                
                ],


        [
        sg.Text('pros', size =(4, 1)), 
        sg.InputText(key="pros_0",
                    font=("helvetica,14"),
                    size=(30,1)), 
        sg.Slider(enable_events=True,
                    key= "slider_pros_0", 
                    orientation = "horizontal",
                    size = (6,10),),

        sg.Text('cons', size =(4, 1)), 
        sg.InputText(key="cons_0",
        font=("helvetica,14"),
        size=(30,1)), 
        sg.Slider(enable_events=True,key= "slider_cons_0", 
        orientation = "horizontal",size = (6,10),),
        
        sg.Text("Linking Words for Results", 
                key="linking_words_results1",
                enable_events=True,
                size= (None,None),
                ),
      
        ],
    
        [
        sg.Text('pros', size =(4, 1)), 
        sg.InputText(key="pros_1",
                    size=(30,1),
                    font=("helvetica,14"),

                    ), sg.Slider(enable_events=True,key= "slider_pros_1", orientation = "horizontal",size = (6,10),),
        sg.Text('cons', size =(4, 1)), 
        sg.InputText(key="cons_1",
                    size=(30,1),
                    
                    font=("helvetica,14"),
                    
                    ), 
        sg.Slider(enable_events=True,
                    key= "slider_cons_1", 
                    orientation = "horizontal",
                    size = (6,10),),
        sg.Text("Connecting Words for Emphasis", 
                key="connecting_words_emphasis",
                enable_events=True,
                size= (None,None),
                )
        ],
        
        [
        sg.Text('pros', size =(4, 1)), 
        sg.InputText(key="pros_2",
                    font=("helvetica,14"),
                    size=(30,1)), 
        sg.Slider(enable_events=True,
                    key= "slider_pros_2", 
                    orientation = "horizontal",size = (6,10),),
        sg.Text('cons', size =(4, 1)), 
        sg.InputText(key="cons_2",
                font=("helvetica,14"),
            size=(30,1)), 
        sg.Slider(enable_events=True,
                    key= "slider_cons_2", 
                    orientation = "horizontal",
                    size = (6,10),),
        sg.Text("Linking Words for Addition", 
                key="linking_words_addition",
                enable_events=True,
                size= (None,None),
                )
        ],

        [
        sg.Text('pros', size =(4, 1)), 
        sg.InputText(key="pros_3",
            font=("helvetica,14"),
            size=(30,1)), 
        sg.Slider(enable_events=True,
                    key= "slider_pros_3", 
                    orientation = "horizontal",
                    size = (6,10),),
        
        sg.Text('cons', size =(4, 1)), 
        sg.InputText(key="cons_3",
                    font=("helvetica,14"),
                    size=(30,1)), 
        sg.Slider(enable_events=True,
                    key= "slider_cons_3", 
                    orientation = "horizontal",
                    size = (6,10),),
        sg.Text("Connecting Words for Illustration", 
                key="connecting_words_illustration",
                enable_events=True,
                size= (None,None),
                ),



        ],

        [
        sg.Text('pros', size =(4, 1)), 
        sg.InputText(key="pros_4",
                    font=("helvetica,14"),
                    size=(30,1)), 
        sg.Slider(enable_events=True,
                    key= "slider_pros_4", 
                    orientation = "horizontal",
                    size = (6,10),),
        sg.Text('cons', size =(4, 1)), 
        sg.InputText(key="cons_4",
                    font=("helvetica,14"),
                    size=(30,1)), 
        sg.Slider(enable_events=True,
                key= "slider_cons_4", 
                orientation = "horizontal",
                size = (6,10),),
        sg.Text("Linking Words for Contrast", 
                key="linking_words_contrast",
                enable_events=True,
                size= (None,None),
                )

        ],


        [
        sg.Text('pros', size =(4, 1)), 
        sg.InputText(key="pros_5",
                    font=("helvetica,14"),
                    size=(30,1)), 
        sg.Slider(enable_events=True,key= "slider_pros_5", orientation = "horizontal",size = (6,10),),
        sg.Text('cons', size =(4, 1)), 
        sg.InputText(key="cons_5",
                    font=("helvetica,14"),
                    size=(30,1)), 
        sg.Slider(enable_events=True,
                    key= "slider_cons_5", 
                    orientation = "horizontal",
                    size = (6,10),),
        sg.Text("Linking Words for Reason", 
                key="linking_words_reason",
                enable_events=True,
                size= (None,None),
                ),
       

        ],
        [
        sg.Text('pros', size =(4, 1)), 
        sg.InputText(key="pros_6",
                    font=("helvetica,14"),
                    size=(30,1)), 
        sg.Slider(enable_events=True,
                    key= "slider_pros_6", 
                    orientation = "horizontal",
                    size = (6,10),),
        sg.Text('cons', size =(4, 1)), 
        sg.InputText(key="cons_6",
                    font=("helvetica,14"),
                    size=(30,1)), 
        sg.Slider(enable_events=True,
                    key= "slider_cons_6", 
                    orientation = "horizontal",
                    size = (6,10),),
        sg.Text("Linking Words for Comparison", 
                key="linking_words_comparison",
                enable_events=True,
                size= (None,None),
                )
        ],

### summary of slider
        [sg.Text("",size=(44,1)), sg.Text("Sum of pros",justification="left", size= (10,1)), sg.Text("?",key="sum_of_pros"),
sg.Text("",size=(34,1)), sg.Text("Sum of cons",justification="left", size=(10,1)), sg.Text("?",key="sum_of_cons"),
        ],

### analysis
        [sg.Multiline(key="analysis",size =(40,5),tooltip="This is a multiline on line 1259 of the code",font =("helvetica", 14)), ],
        [sg.Button("save analysis to CSV",size =(40,1),tooltip="TODO add student name to file save")]
   

    ])





#create empty list
tracker_layout = []

#generate the tab content
#produce 0-4
# TODO needs to produce a text file with all of the keys as text
tracker_layout.append(      
                [
                sg.Text("Grammar issues",size=(40,1),
                tooltip = "nothing to Click to change this item.",
                enable_events=False,
                font=("helvetica",20)),
                sg.Button("edit common errors file",tooltip="click to open editor")
                ],

  )

# TODO this should generate all required if event == "x"   
# see line 1396 for reference
# label
# input
# slider      
# window["input1"].update(hold_json[most_recent_date]["passive voice"]  )

# for passing data to the json file
# 

for x in range(0,len(top_ten)//2):
    tracker_layout.append(        
        [
        sg.Text(top_ten[x],key="label"+ str(x),auto_size_text = True, size =(10, 1)), 
        sg.InputText(key="input"+ str(x) ,size=(40,2), tooltip = "input"+ str(x)), 
        sg.Slider(enable_events=True,key= "grammar_slider"+ str(x),tooltip = "grammar_slider"+ str(x) ,   orientation = "horizontal",size = (6,10),),
        
        sg.Text(top_ten[x+5],key="label"+ str(x+5),auto_size_text = True, size =(10, 1)), 
        sg.InputText(key="input"+ str(x+5) ,size=(40,2),tooltip = "input"+ str(x+5)   ), 
        sg.Slider(enable_events=True,key= "grammar_slider"+ str(x+5), tooltip = "grammar_slider"+ str(x+5) , orientation = "horizontal",size = (6,10),),
        ],
        )


tracker_layout.append(
        [
        sg.Text("performance sum",justification="right", size=(None,None)), sg.Input("0",key="performance sum"),
        ],
                    )

tracker_layout.append(
        [sg.Multiline(key="grammar analysis",
                        default_text='put the grammar analysis here',
                        size =(40,5),
                        tooltip="This is a multiline object key grammar analysis",
                        font =("helvetica", 14)), 
        sg.Button("save grammar analysis",
                        tooltip="saves JSON")],
                     )
tracker_layout.append(
        [sg.Multiline(key="vocabulary_used",
                        default_text='put vocabulary words here',

                        size =(40,5),
                        tooltip="key vocabulary_used",
                        font =("helvetica", 14)), 
                        
        ],
                    )   


# tracker_layout.append(grammar_column_left)


#grammar_tracker_tab= sg.Tab ("grammar tracker",tracker_layout,grammar_column_left,grammar_column_right)
grammar_tracker_tab= sg.Tab ("grammar tracker",tracker_layout)

# question tab layout
# BUG KeyError: 'anything everything nothing something'
# bug KeyError: 'intermediate English'

worksheet_tab_layout = [


        [sg.Text("Worksheet"), 
        sg.Text("instructions:"),
        ],
                
        [sg.Text("select one category"), 
        sg.Combo(values=category_list, 
                # this key event must be unique so how to call it in events?
                # if db_category in event?
                key="db_category", 
                enable_events=True, 
                size=(None,None), 
                tooltip="line 1568 key=db_category" ), 
                sg.Text("Database info:"), # pulling from new db
                sg.Text("", key= "questions_db_info",size=(20,1)),
                 ],

        [sg.Text("selected topics instructions", tooltip="line 1575 TODO start pulling from new DB")],
        
        [sg.Multiline(default_text="Welcome! You are about to experience\none of the most advanced English classes ever.", 
                    key="question_instructions", 
                    font = ("helvetica",13),
                    tooltip ="TODO I want to be able to write/update changes here,line 1580",
                    size=(None,3 ),
                    change_submits=True, 
                    # expand_y=True, 
                    disabled=True ), 
        sg.Button("Open\ninstructions\nfile",
                    size=(18,5),
                    key ="open_question_instructions",
                    tooltip="line1588 key = open_question_instructions"),

        ],
        
     

        
        #start question area
        # layout is ugly
       # prompt 1
        [sg.Text("---------------prompt 1-------------------")],        
        [sg.Multiline("This will be populated by the db. Here is a a really long prompt to check if the UI can handle it.: ",
                    key ="worksheet_prompt1",
                    tooltip = "key worksheet_prompt1 1599",
                    # TODO set meaningful key
                    size = (None,2),
                    font=("helvetica"),
                    ),
        sg.Button("get next question", 
                    #hopefully
                    # this should be aware of previously used questions
                    # This should ideally NOT pull a question that has already been seen by the student.
                    key="get_next_random_question1", 
                    button_color="red",
                    size=(20,1)),
        ],


        [
        sg.Text("question #: ",
                tooltip = "q # pulled from db line 1384"
                ),
        sg.Text("",key="worksheet_question_number1"), 
        # sg.Text("flag",tooltip="line1611"),
        #TODO identify radio groupname
        sg.Radio('needs attention', "worksheet_RADIO1",  
                key="worksheet_needs_attention1", 
                default=False, 
                size=(None,None)),
        
        ], 
       
        [sg.Multiline("This is where the student response goes.",
                # get student input
                # this can then be added to the db if time allows
                # size none is not using full
                # this is where the student' input goes
                size =(None,1),
                key="prompt_response1",
                font=("helvetica"), 
                tooltip="prompt_response1 line 1637"
                ),
        
        sg.Button("Save prompt response 1",
                button_color="green",
                key="save_prompt_response1",
                ),
        ],



        [sg.Button("generate grammar graph",
                    key = "display_grammar_graph_prompt_response1",
                    size=(20,1),
                    tooltip="TODO generate clickable button link in UI line 1646",

                    ) ,

        sg.Button("view generated grammar graph",
                    key = "view_grammar_graph_prompt_response1",
                    size=(25,1),
                    tooltip="TODO link to grammar graph line 1653",

                    ) ,

        
        ],

        
       # prompt 2
[sg.Text("---------------prompt 2-------------------")],        
        [sg.Multiline("This will be populated by the db. Here is a a really long prompt to check if the UI can handle it.: ",
                    key ="worksheet_prompt2",
                    tooltip = "key worksheet_prompt2 1666",
                    
                    # TODO set meaningful key
                    size = (None,2),
                    font=("helvetica"),
                    ),
        sg.Button("get next question", 
                    #hopefully
                    key="get_next_random_question2", 
                    button_color="red",
                    size=(20,1)),
        ],


        [
        sg.Text("question #: ",
                tooltip = "q # pulled from db line 1687"
                ),
        sg.Text("",key="worksheet_question_number2"),   
            
        #TODO identify radio groupname
        sg.Radio('needs attention', "worksheet_RADIO2", 
                key="worksheet_needs_attention2", default=False, size=(None,None)),
        
        ], 
       
        [sg.Multiline("This is where the student response goes.",
                # get student input
                # this can then be added to the db if time allows
                # size none is not using full
                size =(None,1),
                key="prompt_response2",
                font=("helvetica"), 
                tooltip="prompt_response2 line 1703"
                ),
        
        sg.Button("Save prompt response 2",
                button_color="green",
                key="save_prompt_response2",
                ),
        ],



        [sg.Button("display grammar graph",
                    key = "display_grammar_graph_prompt_response2",
                    size=(20,1),
                    tooltip="line 1684",

                    ) ,
         sg.Button("view generated grammar graph",
                    key = "view_grammar_graph_prompt_response2",
                    size=(25,1),
                    tooltip="1999 TODO link to grammar graph line 1722",

                    ) ,
        
        ],



        #bottom of the tab
        [sg.Button("open attention csv",
        tooltip ="line 2009",
        key="open_attention_csv"),
        ]


        
    ]

#end of worksheet tab layout

# --- end of worksheet layout

worksheet_tab= sg.Tab ("worksheet",worksheet_tab_layout)



question_tab_layout = [


        [sg.Text("HOMEWORK"), sg.Text("instructions:")],
                
        [sg.Text("select one category"), 
        sg.Combo(values=category_list, 
                key="db_category", 
                enable_events=True, 
                size=(None,None), 
                tooltip="line 2035 key=db_category" ), 
                sg.Text("Database info:"),
                sg.Text("", 
                        key= "questions_db_info",
                        size=(20,1)),
                 ],

        [sg.Text("selected topics instructions", tooltip="line 1369")],
        
        [sg.Multiline(default_text="Welcome! You are about to experience\none of the most advanced English classes ever.", 
                    key="question_instructions", 
                    font = ("helvetica",13),
                    tooltip ="2045 TODO I want to be able to write/update changes here,line 1748\nmaybe new DB will allow me to do that!",
                    size=(None,3 ),
                    change_submits=True, 
                    # expand_y=True, 
                    disabled=True ), 
            sg.Button("Open\ninstructions\nfile",
                        size=(None,3),
                        key ="open_question_instructions",
                        tooltip="line 2053 key = open_question_instructions"),

        ],
        
        #done link to open the instructions csv 
        # /home/dgd/Desktop/EnglishHelpsYourCareer/category_instructions.csv
        # done button to save the current question number for future review
        
             

        [sg.Text("question #: ",
                tooltip = "q # pulled from db line 1699"
                ),
        sg.Text("",key="db_question_number"), 
        # sg.Text("flag",tooltip="line1700"),
        sg.Radio('needs attention', 
                    "RADIO2", 
                    key="needs_attention", 
                    default=False, 
                    size=(None,None)),
        sg.Button("open attention csv",
                key="open_attention_csv"), 
        ],
        
        [ sg.Multiline("",
                key="db_question",
                size=(None,3),
                disabled = True,
                justification="left",
                font=("helvetica",13),
                tooltip="line 2078")
        ],
        
        [sg.Button("1 show possible answers",
                    button_color="green",
                    key="show_possible_answers",
                    size=(20,1),
                    ),
                    sg.Text("! indicates wrong answers separate answers with ;",visible=False),

        sg.Button("display correct answer",
                    size=(20,1),
                    button_color="yellow",

                    font=('helvetica'),
                    tooltip="line 2093",
                    ) ,

        sg.Button("get next question", 
                    key="get_next_random_question", 
                    button_color="red",
                    size=(20,1)),
        # sg.Button("advance to next question", 
        #             #done set up button to go ahead as content can be repetitive
        #             key="advance_to_next_random_question", 
        #             size=(20,1)),

        ],

        [
        sg.Text("???",
                visible=False,
                key="correct_answer",
                font = ("helvetica",28)
                # size=(80,1),

                )
        ],

        
        #start question area
        [sg.Text("Possible Answers: ",
                    font=("helvetica",18)),
        sg.Input("",
                # get student input
                # this can then be added to the db if time allows
                key="student_answer1",
                font=("helvetica",18), 
                tooltip="student_answer1 line 2126"
                ), 
                
                sg.Text("! indicates wrong answers separate answers with ;"),
        ],
        
        [
        sg.Text("01: ", 
                font=("helvetica",18)),
        
        sg.Text("?",
                key= "db_choice1", 
                font=("helvetica",18), 

                enable_events=True,
                size=(None,None),
                )
        ],

        [sg.Text("02: ",
            font=("helvetica",18)),
            sg.Text("?",
                    key= "db_choice2",
                    font=("helvetica",18), 
                    enable_events=True,
                    size=(None,None))],
        [sg.Text("03: ", font=("helvetica",18) ),
            sg.Text("?",
                    key= "db_choice3",
                    font=("helvetica",18), 
                    enable_events=True,
                    size=(None,None))],
        [sg.Text("04: ", font=("helvetica",18)),
            sg.Text("?",
                    key= "db_choice4",
                    font=("helvetica",18), 
                    enable_events=True,
                    size=(None,None))],
        [sg.Text("05: ", font=("helvetica",18)),sg.Text("", font=("helvetica",18),key= "db_choice5",enable_events=True,size=(None,None))],
        # [sg.Text("06: "),sg.Text("?",key= "db_choice6",enable_events=True,size=(None,None))],
        # [sg.Text("07: "),sg.Text("?",key= "db_choice7",enable_events=True,size=(None,None))],
        # [sg.Text("08: "),sg.Text("?",key= "db_choice8",enable_events=True,size=(None,None))],
        # [sg.Text("09: "),sg.Text("?",key= "db_choice9",enable_events=True,size=(None,None))],
        # [sg.Text("10: "),sg.Text("?",key= "db_choice10",enable_events=True,size=(None,None))],
        [sg.Text("Put first choice here: "),
        sg.Input(default_text="answer?",
        key= "student_question_choice")],
        
        #handle the buttons at the bottom of the screen
        [
        sg.Button("display grammar graph",
                    # this should open the file 
                    key = "display_grammar_graph",
                    size=(40,1),
                    tooltip="line 2178",

                    ) ,

        sg.Button("save and export",
                    key="export_student_questions",
                    tooltip="2193 key export student questions",
                    size=(30,1))
        ],
        
    ]

#end of question tab layout

question_tab= sg.Tab ("questions", 
                    question_tab_layout, 
                    #looks like tooltips don't work with tabs
                    tooltip="test")



### layout
layout = [
    
    #done column with image and text 
    [sg.Menu(menu_def, tearoff=True)],
    
    # file is /home/dgd/Desktop/python_storyboard_flashcards/students/student_names.txt
    [sg.Text("student name:"),
            sg.Combo(values=student_names,
                   key="student_name",
                    default_value="Horst",

                    tooltip="key student_name",
            ), 
    
    sg.Button("load student json", 
                tooltip = "see line 2226",

                ) ,

    sg.Text("date picker: ",
            tooltip="TODO this needs to load from the json file line 2231",), 
    
    sg.Combo(values=[""], 
            size = (20,1),
            key = "date_picker", 
            enable_events=True,
            tooltip="loads from the json file line 2237"),
    sg.Button("load syllabus", 
            #this opens the md syllabus file
            tooltip="will open md file in VS code line 2240"),
    
    sg.Button("TODO worksheet",
            key="TODO_worksheet",
            tooltip="2297" ),

    sg.Button("start timer",
                key = "start timer",
                tooltip = "2300"
                )

    
    ],

    [sg.TabGroup([[tab_one,
                    storyboard_tenses_tab_two,
                    new_negotiation_tab,
                    #negotiation_tab_three,
                    timeline_tab, 
                    pros_cons_tab,
                    question_tab ,
                    worksheet_tab, 
                    grammar_tracker_tab,
                    ]],key="tabgroup"),],
   
]
    


window = sg.Window('Development version! DATE: '+ datetime.date.today().strftime("%Y %B %d %A ") + 'contact Dennis@\nEnglishHelpsYourCareer.com', 
                    
                    layout, 
                    background_color="lightblue",
                    size = (1100,700),
                    
                    location=(1800, 50),
                    default_element_size=(35, 1), 
                    grab_anywhere=True)
# big loop
while True:


    event, values = window.read(timeout=25)


    # if event == sg.TIMEOUT_EVENT:
    #     window.Element('test_gif').UpdateAnimation(test_gif,  time_between_frames=50)

    if event == "TODO_worksheet":
                os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/worksheet_tab/TODO_worksheet_tab.md"))

# pros cons tab
    if event == "pros_cons_issues":
        read_list_from_file()
        with open("/home/dgd/Desktop/python_storyboard_flashcards/pros_cons_tab/pros_cons_events.md") as myfile:
            lines = myfile.readlines()
        selected_topic = random.choice(lines).strip()
        window["pros_cons_issues"].update(selected_topic)



# menu item Linking Words    
    if event == "linking_words_results":
        read_list_from_file()
        with open("/home/dgd/Desktop/python_storyboard_flashcards/word_lists/linking_words_results.md") as myfile:
            lines = myfile.readlines()
        selected_topic = random.choice(lines).strip()
        window["linking_words_results"].update(selected_topic)
        
    if "connecting_words_concession" in event:
        read_list_from_file()
        open_generic_file("/home/dgd/Desktop/python_storyboard_flashcards/word_lists/connecting_words_concession.md","connecting_words_concession")
    

    if  "connecting_words_summary" in event:
        read_list_from_file()
        open_clean_save("/home/dgd/Desktop/python_storyboard_flashcards/word_lists/connecting_words_summarizing.md")
        # open_generic_file("/home/dgd/Desktop/python_storyboard_flashcards/word_lists/connecting_words_summary.md","connecting_words_summary")
        
  
    if event == "connecting_words_emphasis":
        read_list_from_file()
        with open("/home/dgd/Desktop/python_storyboard_flashcards/word_lists/connecting_words_emphasis.md") as myfile:
            lines = myfile.readlines()
        selected_topic = random.choice(lines).strip()
        window["connecting_words_emphasis"].update(selected_topic)
        

    if event == "connecting_words_illustration":
        read_list_from_file()
        with open("/home/dgd/Desktop/python_storyboard_flashcards/word_lists/connecting_words_illustration.md") as myfile:
            lines = myfile.readlines()
        selected_topic = random.choice(lines).strip()
        window["connecting_words_illustration"].update(selected_topic)

    

    if event == "linking_words_addition":
        read_list_from_file()
        with open("/home/dgd/Desktop/python_storyboard_flashcards/word_lists/linking_words_addition.md") as myfile:
            lines = myfile.readlines()
        selected_topic = random.choice(lines).strip()
        window["linking_words_addition"].update(selected_topic)


    if event == "linking_words_comparison":
        read_list_from_file()
        with open("/home/dgd/Desktop/python_storyboard_flashcards/word_lists/linking_words_comparison.md") as myfile:
            lines = myfile.readlines()
        selected_topic = random.choice(lines).strip()
        window["linking_words_comparison"].update(selected_topic)

    if event == "linking_words_condition":
        read_list_from_file()
        open_generic_file("/home/dgd/Desktop/python_storyboard_flashcards/word_lists/linking_words_condition.md","linking_words_condition")
       
        
    if event == "linking_words_contrast":
        read_list_from_file()
        with open("/home/dgd/Desktop/python_storyboard_flashcards/word_lists/linking_words_contrast.md") as myfile:
            lines = myfile.readlines()
        selected_topic = random.choice(lines).strip()
        window["linking_words_contrast"].update(selected_topic)


    if event == "linking_words_reason":
        read_list_from_file()
        with open("/home/dgd/Desktop/python_storyboard_flashcards/word_lists/linking_words_reason.md") as myfile:
            lines = myfile.readlines()
        selected_topic = random.choice(lines).strip()
        window["linking_words_reason"].update(selected_topic)



    if "linking_words_results" in event:
        read_list_from_file()
        # open_generic_file("/home/dgd/Desktop/python_storyboard_flashcards/word_lists/linking_words_results.txt","linking_words_results")
        os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/word_lists/linking_words_results.md"))





# pros cons tabs
    if event == "edit pros cons issues":
        os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/pros_cons_tab/pros_cons_events.md"))

    if event == "soft skills list":
        os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/EnglishHelpsYourCareer/topic_soft_skills.md"))



    if event == "new topic":
        new_topic = sg.PopupGetText("enter new topic")
        #pros_cons_issues
        window["pros_cons_issues"].update(new_topic)
        selected_topic = new_topic

# grammar tracker tab events

    if "grammar_slider" in event:
        #update performance sum field
        window["performance sum"].update(values["grammar_slider0"]+
                                         values["grammar_slider1"]+
                                         values["grammar_slider2"]+
                                         values["grammar_slider3"]+
                                         values["grammar_slider4"]+
                                         values["grammar_slider5"]+
                                         values["grammar_slider6"]+
                                         values["grammar_slider7"]+
                                         values["grammar_slider8"]+
                                         values["grammar_slider9"]
                                        )


    if event == "date_picker":
        student_name = values["student_name"]
        if student_name == "":
            sg.PopupError("No student json file by that name", 
                            location=(2000, 100),)
            continue
        json_files = glob.glob("/home/dgd/Desktop/python_storyboard_flashcards/students/*.json"  )
        # print (json_files)
        for x_file in json_files:
            #TODO allow users to enter new students through UI
            
            if x_file.endswith(student_name+".json"):
                # sg.PopupOK("found it",
                # location=(2000, 100),)
                break
        else:
            sg.PopupError("not found",
                        location=(2000, 100), )
            continue
        # all ok we found the JSON
        # x_file
        # BUG need to catch errors without crashing
        # KeyError: 'questions'
        with open(x_file) as my_file:
            hold_json = json.load(my_file)
        print(hold_json)
        # most_recent_date = max(hold_json.keys())
        most_recent_date = values["date_picker"]
        # populate gui with JSON data
        # first yellow is gui key
        # second yellow is key of json
        
        # TODO get the dates as a list in the combo box at line 1316
        # testing date picker 

        # window["date_picker"].update(values = list(hold_json.keys()))

        # window["date_picker"].update(most_recent_date)

        window["grammar analysis"].update(hold_json[most_recent_date]["grammar analysis"]  )
        window["vocabulary_used"].update(hold_json[most_recent_date]["vocabulary_used"]  )
        window["performance sum"].update(hold_json[most_recent_date]["performance sum"]  )
        window["input0"].update(hold_json[most_recent_date]["passive voice"][0])
        window["input1"].update(hold_json[most_recent_date]["conditionals"][0])
        window["input2"].update(hold_json[most_recent_date]["questions"][0])
        # window["input2"].update(hold_json[most_recent_date]["articles"][0])
        window["input3"].update(hold_json[most_recent_date]["modals"][0])
        window["input4"].update(hold_json[most_recent_date]["connecting words"][0])
        window["input5"].update(hold_json[most_recent_date]["prepositions"][0])
        window["input6"].update(hold_json[most_recent_date]["comparatives and superlatives"][0])
        window["input7"].update(hold_json[most_recent_date]["phrasal verbs"][0])
        window["input8"].update(hold_json[most_recent_date]["irregular verbs"][0])
        window["input9"].update(hold_json[most_recent_date]["pronunciation"][0])
        #handle slider values of grammar tracker 
        # [1] get second element of list
        window["grammar_slider0"].update(hold_json[most_recent_date]["passive voice"][1])
        window["grammar_slider1"].update(hold_json[most_recent_date]["conditionals"][1])
        window["grammar_slider2"].update(hold_json[most_recent_date]["questions"][1])
        # window["grammar_slider2"].update(hold_json[most_recent_date]["articles"][1])
        window["grammar_slider3"].update(hold_json[most_recent_date]["modals"][1])
        window["grammar_slider4"].update(hold_json[most_recent_date]["connecting words"][1])
        window["grammar_slider5"].update(hold_json[most_recent_date]["prepositions"][1])
        window["grammar_slider6"].update(hold_json[most_recent_date]["comparatives and superlatives"][1])
        window["grammar_slider7"].update(hold_json[most_recent_date]["phrasal verbs"][1])
        window["grammar_slider8"].update(hold_json[most_recent_date]["irregular verbs"][1])
        window["grammar_slider9"].update(hold_json[most_recent_date]["pronunciation"][1])



    if event == "load student json":
        # BUG crashes intermittently
        # TODO need a log catcher
        student_name = values["student_name"]
        if student_name == "":
            sg.PopupError("No student json file by that name", 
                            location=(2000, 100),)
            continue
        json_files = glob.glob("/home/dgd/Desktop/python_storyboard_flashcards/students/*.json"  )
        # print (json_files)
        for x_file in json_files:
            #TODO allow users to enter new students through UI
            # 
            if x_file.endswith(student_name+".json"):
                sg.PopupOK("found it",
                location=(2000, 100),)
                break
        else:
            sg.PopupError("not found",
                        location=(2000, 100), )
            continue
        # all ok we found the JSON
        # x_file
        with open(x_file) as my_file:
            hold_json = json.load(my_file)
        print(hold_json)
        most_recent_date = max(hold_json.keys())
        # populate gui with JSON data
        # first yellow is gui key
        # second yellow is key of json
        
        # done get the dates as a list in the combo box at line 
        # testing date picker 

        window["date_picker"].update(values = list(hold_json.keys()))

        window["date_picker"].update(most_recent_date)
        
        window["grammar analysis"].update(hold_json[most_recent_date]["grammar analysis"]  )
        window["vocabulary_used"].update(hold_json[most_recent_date]["vocabulary_used"]  )
        window["performance sum"].update(hold_json[most_recent_date]["performance sum"]  )
        window["input0"].update(hold_json[most_recent_date]["passive voice"][0])
        window["input1"].update(hold_json[most_recent_date]["conditionals"][0])
        #todo KeyError: 'articles'
        #can't create new JSON
        # this file is NOT being updated based on the common error file :(
        window["input2"].update(hold_json[most_recent_date]["questions"][0])
        # window["input2"].update(hold_json[most_recent_date]["articles"][0])
        window["input3"].update(hold_json[most_recent_date]["modals"][0])
        window["input4"].update(hold_json[most_recent_date]["connecting words"][0])
        window["input5"].update(hold_json[most_recent_date]["prepositions"][0])
        window["input6"].update(hold_json[most_recent_date]["comparatives and superlatives"][0])
        window["input7"].update(hold_json[most_recent_date]["phrasal verbs"][0])
        window["input8"].update(hold_json[most_recent_date]["irregular verbs"][0])
        window["input9"].update(hold_json[most_recent_date]["pronunciation"][0])
        #handle slider values of grammar tracker 
        # [1] get second element of list
        window["grammar_slider0"].update(hold_json[most_recent_date]["passive voice"][1])
        window["grammar_slider1"].update(hold_json[most_recent_date]["conditionals"][1])
        window["grammar_slider2"].update(hold_json[most_recent_date]["questions"][1])
        # window["grammar_slider2"].update(hold_json[most_recent_date]["articles"][1])
        window["grammar_slider3"].update(hold_json[most_recent_date]["modals"][1])
        window["grammar_slider4"].update(hold_json[most_recent_date]["connecting words"][1])
        window["grammar_slider5"].update(hold_json[most_recent_date]["prepositions"][1])
        window["grammar_slider6"].update(hold_json[most_recent_date]["comparatives and superlatives"][1])
        window["grammar_slider7"].update(hold_json[most_recent_date]["phrasal verbs"][1])
        window["grammar_slider8"].update(hold_json[most_recent_date]["irregular verbs"][1])
        window["grammar_slider9"].update(hold_json[most_recent_date]["pronunciation"][1])


#menu items
    if event == "Open_docs":
        os.system("{} {}".format(FIREFOX,"https://pysimplegui.readthedocs.io/en/latest/",new=2,autoraise=True ))
                
    if event == 'README':
        os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/README.md"))

    if event == 'tips':
        os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/tips.md"))

    if event == "load syllabus":
        os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/EnglishHelpsYourCareer/30_week_syllabus.md"))

    # this opens a new web browser
    # if event == "load syllabus":
    #     subprocess.Popen(['firefox',"https://cnn.com"]) #f"{} {}".format(firefox, "https://cnn.com"))



    if event == "start timer":
        os.system("gnome-clocks")

    if event == "core vocab":
        webbrowser.open("https://docs.google.com/spreadsheets/d/1XfMVJNB4UMy0NU5QteYEUZkmfRUIVNSf19ZuC5A23T8/edit#gid=0",new=1,autoraise=True )
    #     os.system("{} {}".format(FIREFOX,"https://pysimplegui.readthedocs.io/en/latest/",new=2,autoraise=True ))

    # if event == "core vocab":
    #     webbrowser.firefox("https://docs.google.com/spreadsheets/d/1XfMVJNB4UMy0NU5QteYEUZkmfRUIVNSf19ZuC5A23T8/edit#gid=0",new=1,autoraise=True )
    #     os.system("{} {}".format(FIREFOX,"https://pysimplegui.readthedocs.io/en/latest/",new=2,autoraise=True ))



    if event == "2 letter words":
        webbrowser.open("https://docs.google.com/spreadsheets/d/12_mq9Pp5VSyrYeXf1qxsZGXrF22fOI4yQksBoziaT9g/edit?usp=sharing",new=0,autoraise=True )

    if event == "3 letter words":
        webbrowser.open("https://docs.google.com/spreadsheets/d/1YZcrl4TU9LKJnaSP-HLUtZkFLuq4cZkU8eCR-X2WwG0/edit?usp=sharing",new=2,autoraise=True )
        # pass

    if event == "4 letter words":
        #https://docs.google.com/spreadsheets/d/1RYO8jChzmU09rFI5hq57e8u3LKn7JIsq7xXggGakZtE/edit?usp=sharing
        webbrowser.open("https://docs.google.com/spreadsheets/d/1RYO8jChzmU09rFI5hq57e8u3LKn7JIsq7xXggGakZtE/edit?usp=sharing",new=2,autoraise=True )

# pronunciation

    if event == 'pron_soft_d':
        os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/word_lists/pron_ed_soft_d_sound.md")),

    if event == 'pron_ed_id':
        os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/word_lists/pron_ed_id_sound.md")),

    if event == 'pron_ed_t':
        os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/word_lists/pron_ed_t.md")),



    if event == 'silent_b':
        os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/word_lists/silent_b.md")),

    if event == 'pron_k':
        os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/word_lists/pron_ed_k.md")),

    if event == 'silent_s':
        os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/EnglishHelpsYourCareer/students/English_pronunciation_tips.md")),

    # /home/dgd/Desktop/EnglishHelpsYourCareer/students/English pronunciation tips.md
    if event == 'misc_pronunciation':
        os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/EnglishHelpsYourCareer/students/English_pronunciation_tips.md")),

# linking word

    if event == 'M_addition':
        os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/word_lists/linking_words_addition.md")),

    if event == 'M_comparison':
        os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/word_lists/linking_words_comparison.md")),



    if event == 'M_condition':
        os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/word_lists/linking_words_condition.md")),

    if event == 'M_concenssion':
        os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/word_lists/connecting_words_concession.md")),

    if event == 'M_coordinating':
        os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/word_lists/coordinating_conjunctions.md")),
    
    if event == 'M_contrast':
        os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/word_lists/linking_words_contrast.md")),

    if event == 'M_emphasis':
        os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/word_lists/connecting_words_emphasis.md")),

    if event == 'M_illustration':
        os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/word_lists/connecting_words_illustration.md")),

    if event == 'M_reason':
        os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/word_lists/connecting_words_emphasis.md")),


    if event == 'M_results':
        os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/word_lists/linking_words_results.md")),

    if event == 'M_subordinating':
        os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/word_lists/subordinating_conjunctions.md")),

    if event == 'M_summarizing':
        os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/word_lists/connecting_words_summarizing.md")),

# rhyme_site
    # if event == 'rhyme_site':
    #     webbrowser.open("https://www.rhymezone.com/",new=2,autoraise=True )

    if event == "rhyme_site":
        os.system("{} {}".format(FIREFOX,"https://www.rhymezone.com/",new=2,autoraise=True ))
        


# ---------------------------------------question tab events---------------------

    if event == "display_grammar_graph":
        question = values["db_question"]
        question_number = window["db_question_number"].DisplayText


        sentence_nlp = nlp(question)
        svg = displacy.render(sentence_nlp, 
                                options = {"compact": True},
                                style="dep")
        output_path = Path(f"/home/dgd/Desktop/python_storyboard_flashcards/question_tab/{question_number}.{question}.svg") # you can keep there only "dependency_plot.svg" if you want to save it in the same folder where you run the script 
        output_path.open("w", encoding="utf-8").write(svg)
        #brave-browser
        # os.system("{} {}".format("brave-browser",f"/home/dgd/Desktop/python_storyboard_flashcards/question_tab/{question_number}.{question}.svg")) 


    if event == "open_question_instructions":
        os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/EnglishHelpsYourCareer/category_instructions.csv"))

    if event == "export_student_questions":
        save_student_answers()
        save_attention()


    if event == "db_choice1":
        window["student_question_choice"].update(window["db_choice1"].DisplayText)

    if event == "db_choice2":
        window["student_question_choice"].update(window["db_choice2"].DisplayText)
    if event == "db_choice3":
            window["student_question_choice"].update(window["db_choice3"].DisplayText)
    if event == "db_choice4":
            window["student_question_choice"].update(window["db_choice4"].DisplayText)
    if event == "db_choice5":
            window["student_question_choice"].update(window["db_choice5"].DisplayText)
    if event == "db_choice6":
            window["student_question_choice"].update(window["db_choice6"].DisplayText)
    if event == "db_choice7":
            window["student_question_choice"].update(window["db_choice7"].DisplayText)
    if event == "db_choice8":
            window["student_question_choice"].update(window["db_choice8"].DisplayText)
    if event == "db_choice9":
            window["student_question_choice"].update(window["db_choice9"].DisplayText)
    if event == "db_choice10":
            window["student_question_choice"].update(window["db_choice10"].DisplayText)
        

    if event == "display correct answer":
        window["correct_answer"].update(visible=True)

    if event == "open_attention_csv":
        os.system("{} {}".format(EXTERNAL_EDITOR, QUESTION_FOLDER + "/needs_attention.csv"))

    if event == "advance_to_next_random_question":
        pass
        #TODO this should advance to next random question without saving the displayed question

    if event == "get_next_random_question":
        save_student_answers()
        save_attention()
        # clear the radio button 
        # clear student choice
        window["needs_attention"].update(False)
        window["student_question_choice"].update("")
        #clear input field
        window["student_answer1"].update("")

        window["correct_answer"].update(visible=False)
        if values["db_category"] not in category_list:
            continue
        print("line",line[0])
        current_question =line[0]
        found = False
        for line in df2.iterrows():
            # my_line = line
            # window["db_question_number"].update(line[0])
            # break        
            
            if line[0]==current_question:
                found=True
                continue
            if found:
                break    
        else:
            sg.PopupOK("all questions used",
                        location=(2000, 100),
                        )
            continue
        # correct question display
        window["db_question_number"].update(line[1]["UNIQUE_ID"]   )
        #filling in choices

        # filter out NANs
        # create list of answers from db
        answers = [
            line[1]["CHOICE 1"], 
            line[1]["CHOICE 2"], 
            line[1]["CHOICE 3"], 
            line[1]["CHOICE 4"], 
            line[1]["CHOICE 5"], 
            line[1]["CHOICE 6"], 
            line[1]["CHOICE 7"], 
            line[1]["CHOICE 8"], 
            line[1]["CHOICE 9"], 
            line[1]["CHOICE 10"], 
        
                    ]

        useful_answers = [a for a in answers if type (a) != float  ]
        print(useful_answers)
        # render all as invisible
        #only display 5 possible answers
        # students can't read options
        for j in range (1,6):
            window[f"db_choice{j}"].update(visible=False)    
                
        # randomize order
        random.shuffle(useful_answers)        
        # iterate over useful answers
        # enumerate start with 1
        for i, u in enumerate(useful_answers):
            window[f"db_choice{i+1}"].update(u)    
            # turn off visibility until user reactivates visiblity
            window[f"db_choice{i+1}"].update(visible=False)    


        window["db_question"].update(line[1]["QUESTION"])
        # make sure correct answer is invisible
        window["correct_answer"].update(visible=False)
        window["correct_answer"].update(line[1]["CORRECT ANSWERS"])

        # display instructions for this category
        # values["db_category"]
        
        try:
            window["question_instructions"].update(instructions[values["db_category"]])
        except KeyError:
                date_string = "{}.{}.{} {}:{}:{}".format(datetime.date.today().year, 
                                        datetime.date.today().month,
                                        datetime.date.today().day,
                                        datetime.datetime.today().hour,
                                        datetime.datetime.today().minute,
                                        datetime.datetime.today().second,)
                window["question_instructions"].update("missing instructions")
                with open(ERROR_LOG_FILENAME, "a") as myfile:
                    myfile.write(f'date: {date_string} | missing instructions: {values["db_category"]}\n')

            
    if event == "show_possible_answers":
         for i, u in enumerate(useful_answers):
            window[f"db_choice{i+1}"].update(u)    
            # toggle visibility
            window[f"db_choice{i+1}"].update(visible=True)  


    if event == "db_category":
        #check if student name is selected
        if values["student_name"] =="":
            sg.PopupError("select student name in above")
            continue
    

        #df holds the question bank dataframe
        #check if valid category
        if values["db_category"] not in category_list:
            continue
        print("category selected: ",values["db_category"])
        selected_category = values["db_category"]
        lines_of_this_cat = df[df['CATEGORY'] == selected_category]
        print("I found questions: ",len(lines_of_this_cat))
        #TODO error catch if column is empty then continue!
        window["questions_db_info"].update(f"I found questions: {len(lines_of_this_cat)}")
        # randomize order 
        # create new df with my_lines 
        # randomize the selection of the database
        my_lines = lines_of_this_cat.sample(len(lines_of_this_cat))
        df2 = my_lines
        #line contains all db choices
        # iterate over the options
        for line in df2.iterrows():
            # my_line = line
            # update line panda created
            window["db_question_number"].update(line[1]["UNIQUE_ID"]   )
            break

        #filling in choices
        # filter out NANs
        # create list of answers from db
        answers = [
            line[1]["CHOICE 1"], 
            line[1]["CHOICE 2"], 
            line[1]["CHOICE 3"], 
            line[1]["CHOICE 4"], 
            line[1]["CHOICE 5"], 
            # line[1]["CHOICE 6"], 
            # line[1]["CHOICE 7"], 
            # line[1]["CHOICE 8"], 
            # line[1]["CHOICE 9"], 
            # line[1]["CHOICE 10"], 
        
                    ]

        useful_answers = [a for a in answers if type (a) != float  ]
        print(useful_answers)
        # render all as invisible
        for j in range (1,6):
            window[f"db_choice{j}"].update(visible=False)    
                
        # randomize order
        random.shuffle(useful_answers)        
        # iterate over useful answers
        # enumarate start with 1
        for i, u in enumerate(useful_answers):
            window[f"db_choice{i+1}"].update(u)    
            # toggle visibility
            window[f"db_choice{i+1}"].update(visible=False)    


        window["db_question"].update(line[1]["QUESTION"])
        # make sure correct answer is invisible
        window["correct_answer"].update(visible=False)
        window["correct_answer"].update(line[1]["CORRECT ANSWERS"])

        # display instructions for this category
        # values["db_category"]
        # getting an error: KeyError: 'pre-intermediate English'
        try:
            window["question_instructions"].update(instructions[values["db_category"]])
        except KeyError:
            date_string = "{}.{}.{} {}:{}:{}".format(datetime.date.today().year, 
                                        datetime.date.today().month,
                                        datetime.date.today().day,
                                        datetime.datetime.today().hour,
                                        datetime.datetime.today().minute,
                                        datetime.datetime.today().second,)
            window["question_instructions"].update("missing instructions")
            with open(ERROR_LOG_FILENAME, "a") as myfile:
                myfile.write(f'date: {date_string} | missing instructions: {values["db_category"]}\n')

            



# ------------------- grammar tracker tab events



# grammar tracker tab



# fire on all pros and con sliders
    if "slider_grammar" in event:
        sum_of_pros = values["slider_pros_0"] + values["slider_pros_1"]+ values["slider_pros_2"]+ values["slider_pros_3"]+ values["slider_pros_4"]+ values["slider_pros_5"]+ values["slider_pros_6"]
        sum_of_cons = values["slider_cons_0"] + values["slider_cons_1"]+ values["slider_cons_2"]+ values["slider_cons_3"]+ values["slider_cons_4"]+ values["slider_cons_5"]+ values["slider_cons_6"]
        # sg.PopupOK(sum_of_pros)
        window["sum_of_pros"].update(sum_of_pros)
        window["sum_of_cons"].update(sum_of_cons)




    if event == "save grammar analysis":
        date_string = "{}.{}.{} {}:{}:{}".format(datetime.date.today().year, 
                                        datetime.date.today().month,
                                        datetime.date.today().day,
                                        datetime.datetime.today().hour,
                                        datetime.datetime.today().minute,
                                        datetime.datetime.today().second,

                                        )

        #empty dict
        content = {}
        for x in range(0,len(top_ten)  ):
            content[top_ten[x]]= [values[f"input{x}"],values[f"grammar_slider{x}"], ]
        # content["summary"]=summary_value
        content["grammar analysis"] = values["grammar analysis"]
        #vocabulary_used
        content["vocabulary_used"] = values["vocabulary_used"]
        content["performance sum"]= values["performance sum"]
        student_progress = {date_string:content}
        #create JSON file
        with open  ( "/home/dgd/Desktop/python_storyboard_flashcards/students/" + values["student_name"]+".json", "a") as myfile:
            json.dump(student_progress,myfile)
        #replacing }{ with comma
        with open ( "/home/dgd/Desktop/python_storyboard_flashcards/students/" + values["student_name"]+".json", "r") as myfile:
            text = myfile.read()
            text = text.replace("}{",",")
        with open ( "/home/dgd/Desktop/python_storyboard_flashcards/students/" + values["student_name"]+".json", "w") as myfile:
            myfile.write(text)

        # TODO generate a simple graph of performance
        # sg.PopupOK("{}.json File saved to directory".format(values["student_name"], 
        #             location  = (1900,50),
        #             )
                    
                #   )
            
# pros cons tab
    # fire on all pros and con sliders
    # TODO this naming structure needs to be updated
    
    
    if event == "clear fields":
        clear_pros_cons()

    
    if ("slider_pros" in event) or ("slider_cons" in event):
        sum_of_pros = values["slider_pros_0"] + values["slider_pros_1"]+ values["slider_pros_2"]+ values["slider_pros_3"]+ values["slider_pros_4"]+ values["slider_pros_5"]+ values["slider_pros_6"]
        sum_of_cons = values["slider_cons_0"] + values["slider_cons_1"]+ values["slider_cons_2"]+ values["slider_cons_3"]+ values["slider_cons_4"]+ values["slider_cons_5"]+ values["slider_cons_6"]
        # sg.PopupOK(sum_of_pros)
        window["sum_of_pros"].update(sum_of_pros)
        window["sum_of_cons"].update(sum_of_cons)

    if event == "save analysis to CSV":
        
        #pull name of topic into name of csv into dictionary
        #pros_cons_issues will have spaces in the file name
        csv_file_name=selected_topic
        if len (csv_file_name)==0:
            sg.PopupError("Name is empty",
                            location=(2000, 100),
                            )
            continue
        
            # append the data to the csv 'a'
        csv_exists = False
        #TODO add student name to file save to PROS cons tab
        if os.path.exists("/home/dgd/Desktop/python_storyboard_flashcards/pros_cons_tab/" + csv_file_name +'.csv'):
            csv_exists = True
        #missing trailing / meant files saved to same directory
        with open("/home/dgd/Desktop/python_storyboard_flashcards/pros_cons_tab/" + csv_file_name +'.csv', 'a', newline='') as csvfile:
        # define field names
            fieldnames = ['topic', 'analysis', 'pro0text','pro0value','con0text','con0value','pro1text','pro1value','con1text','con1value','pro2text','pro2value','con2text','con2value','pro3text','pro3value','con3text','con3value','pro4text','pro4value','con4text','con4value','pro5text','pro5value','con5text','con5value','pro6text','pro6value','con6text','con6value']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if  not csv_exists:
                writer.writeheader()
            writer.writerow({'topic': selected_topic,
                            'analysis': values["analysis"],
                            'pro0text': values['pros_0'] ,
                            'pro0value': values['slider_pros_0'],
                            'con0text': values['cons_0'] ,
                            'con0value': values['slider_cons_0'],
                            'pro1text': values['pros_1'] ,
                            'pro1value': values['slider_pros_1'],
                            'con1text': values['cons_1'] ,
                            'con1value': values['slider_cons_1'],

                            'pro2text': values['pros_2'] ,
                            'pro2value': values['slider_pros_2'],
                            'con2text': values['cons_2'] ,
                            'con2value': values['slider_cons_2'],

                            'pro3text': values['pros_3'] ,
                            'pro3value': values['slider_pros_3'],
                            'con3text': values['cons_3'] ,
                            'con3value': values['slider_cons_3'],

                            'pro4text': values['pros_4'] ,
                            'pro4value': values['slider_pros_4'],
                            'con4text': values['cons_4'] ,
                            'con4value': values['slider_cons_4'],

                            'pro5text': values['pros_5'] ,
                            'pro5value': values['slider_pros_5'],
                            'con5text': values['cons_5'] ,
                            'con5value': values['slider_cons_5'],

                            'pro6text': values['pros_6'] ,
                            'pro6value': values['slider_pros_6'],
                            'con6text': values['cons_6'] ,
                            'con6value': values['slider_cons_6'],


                            })

        sg.PopupOK(f"{csv_file_name}.csv' file written to directory\n{os.getcwd()} dir",
                    location=(2000, 100),
                    )



# tenses tab


    if event in ("irregular verbs", ):
        webbrowser.open("https://docs.google.com/spreadsheets/d/1NM2ZkyO_-DESyWuezXiRqXuKC75qs2Fwxi0mKQbEULY/edit#gid=0",new=2,autoraise=True)

    if event in ("phrasal verbs","phrasal verbs1"):
        webbrowser.open("https://docs.google.com/spreadsheets/d/1K8RfcM_bAnd9WSRIY-2-roiLcXHU37oKtqrwRVHfDgc/edit?usp=sharing",new=2,autoraise=True )
    
    if event in ("collocations", "collocations1"):
        webbrowser.open("https://docs.google.com/spreadsheets/d/1zz38JZhW-ZQ-fj35s14UMiFcWbHehc5CpKe2zIUHDUI/edit?usp=sharing")


    
    if event == "bingo1":
        filename = [file for file in DB_FILES if file.stem == values["bingo1"]][0]
        with filename.open() as myfile:
            lines = myfile.readlines()
        bingo_lines1 = [line.strip() for line in lines if len(line.strip() ) >0    ] 
        window["bingo_text1"].update(value=random.choice(bingo_lines1)) 

    if event == "bingo1_button":
        if values["bingo_text1"] == "":
            continue
        window["bingo_text1"].update(value=random.choice(bingo_lines1)) 


    if event == "bingo2":
        filename = [file for file in DB_FILES if file.stem == values["bingo2"]][0]
        with filename.open() as myfile:
            lines = myfile.readlines()
        bingo_lines2 = [line.strip() for line in lines if len(line.strip() ) >0    ] 
        window["bingo_text2"].update(value=random.choice(bingo_lines2)) 

    if event == "bingo2_button":
        if values["bingo_text2"] == "":
            continue
        window["bingo_text2"].update(value=random.choice(bingo_lines2)) 



    

    if event == "combo_image_filter":
        wanted = values["combo_image_filter"]
        image_list = [name for name in original_image_list if wanted in name]

        window["image_filter_result_number"].update(len(image_list))

    if event == "image_shuffle":
        # check combo_image_filter
        if values["combo_image_filter"] == "":
            image_list = original_image_list
        else:
            wanted = values["combo_image_filter"]
            #list comprehension
            image_list = [name for name in original_image_list if wanted in name]
            print("filtered image list: ", values["combo_image_filter"], len(image_list))
            window["image_filter_result_number"].update(len(image_list))
            print(image_list)
            
            if len(image_list) <6:
                for i in range(len(image_list), 6  ):
                    print(i)
                    image_list.append("/home/dgd/Desktop/python_storyboard_flashcards/random_images/empty_thumbnail.png")
            


        random.shuffle(image_list)
        window["canvas1a"].update(filename=image_list[0])
        window["text1a"].update(split_filename(image_list[0]))
        
        window["canvas1b"].update(filename=image_list[1])
        window["text1b"].update(split_filename(image_list[1]))
        
        window["canvas2a"].update(filename=image_list[2])
        window["text2a"].update(split_filename(image_list[2]))
        
        window["canvas2b"].update(filename=image_list[3])
        window["text2b"].update(split_filename(image_list[3]))
        
        window["canvas3a"].update(filename=image_list[4])
        window["text3a"].update(split_filename(image_list[4]))
        
        window["canvas3b"].update(filename=image_list[5])
        window["text3b"].update(split_filename(image_list[5]))
        

# button in verb adj noun
    if event == "edit verbs list":
        os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/word_lists/verbs.md"))

    if event == "edit nouns list":
        os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/word_lists/nouns.md"))

    if event == "edit adjectives list":
        os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/word_lists/adjectives.md"))

    if event == "edit quantifiers list":
        os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/word_lists/quantifiers.md"))    

    

    if event == "edit basic question words":
        os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/english_question_words.md"))
        webbrowser.open("https://docs.google.com/document/d/1FRGc3k_AkcAbH_w4COKyms9fOjxS7YJfKygv_nin9F4/edit?usp=sharing",new=2,autoraise=True )



    if event == 'reload':
        read_list_from_file()
        window["verbs_list_box"].update(values=verbs_list)
        window["nouns_list_box"].update(values=nouns_list)
        window["adjectives_list_box"].update(values=adjectives_list)
        window["subordinating_conjunctions_list_box"].update(values=subordinating_conjunctions_list)


# button in simple sentence builder
    if event == 'randomize':
        window["verbs_list_box"].update(set_to_index=random.randint(0,len(verbs_list)-1))
        window["nouns_list_box"].update(set_to_index=random.randint(0,len(nouns_list)-1))
        window["adjectives_list_box"].update(set_to_index=random.randint(0,len(adjectives_list)-1))
        window["quantifiers_list_box"].update(set_to_index=random.randint(0,len(quantifiers_list)-1))
        window["subordinating_conjunctions_list_box"].update(set_to_index=random.randint(0,len(subordinating_conjunctions_list)-1))
        # (set_to_index=random.randint(0,len(verbs_list)-1))
        # event, values = window.read()
        # print(window["verbs_list_box"].get())
        result = mermaid_template.format(window["verbs_list_box"].get()[0],
                                        window["adjectives_list_box"].get()[0],
                                        window["nouns_list_box"].get()[0],
                                        window["quantifiers_list_box"].get()[0],   
                                        window["subordinating_conjunctions_list_box"].get()[0],   
                                         )
          
        window['simple_sentence_builder_output'].update(result)

    if event == "save your created sentence":
        filename = values["student_name"]+"_"+datetime.date.today().strftime("%Y %B %d %A") +".txt"        
        with open(filename, 'a') as f:
            #TODO this should be a CSV
            # TODO play with the output as an MD file
            
            f.write(values['simple_sentence_builder_output'])
            f.write("\n")
        filename = values["student_name"]+"_"+datetime.date.today().strftime("%Y %B %d %A") +"_mermaid.txt"        
        with open(filename, 'a') as f:
            #TODO this should be a CSV
            # TODO play with the output as an MD file
            
            f.write(values['simple_sentence_builder_output'])
            f.write("\n")


# Horst's random selection


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





### past tense events


    if event in ("past_simple", "past_simple1"):
        webbrowser.open("https://docs.google.com/spreadsheets/d/1NkmOcQcNU8Dirk_rM04yEF5CS9yaSnYGip0Tyq0AkIU/edit?usp=sharing",new=2,autoraise=True )


    if event == "past_continuous":
        webbrowser.open("https://docs.google.com/spreadsheets/d/14FxeIfy6HA1nFK1HA-t301v-7x2Hf4BoYxnu1hKtm1M/edit?usp=sharing",new=2,autoraise=True )

    if event == "past_perfect_continuous":
        webbrowser.open("https://docs.google.com/spreadsheets/d/1eQYZQA9qWQLEjEwwgBv6hupkzLELxVWXwZEukJ2He2I/edit?usp=sharing",new=2,autoraise=True )

    if event == "past_perfect":
        webbrowser.open("https://docs.google.com/spreadsheets/d/1KzJ68cM0VBsthrfsGJRIXCV4MWXcSIcDdDWfH-Gfl3M/edit?usp=sharing",new=2,autoraise=True )

### present events
    
    if event == "present_simple":
        webbrowser.open("https://docs.google.com/spreadsheets/d/1xv0ZFe6_l66spkXWPyWrzu5k1KPNb3OWKL52Xg71DuE/edit?usp=sharing",new=2,autoraise=True )


    if event == "present_continuous":
        webbrowser.open("https://docs.google.com/spreadsheets/d/1SKgIK56P0qla0l2KEuii35AjPWrg4YJGYqw2prV7BIw/edit?usp=sharing",new=2,autoraise=True )

    if event == "present_perfect_continuous":
        webbrowser.open("https://docs.google.com/spreadsheets/d/1mQoBCdNpjYee6lX5sxwz1oS2xpmkVeimY-CVUnRgxoA/edit?usp=sharing",new=2,autoraise=True )

    if event == "present_perfect":
        webbrowser.open("https://docs.google.com/spreadsheets/d/1vAlXCM5dD8EVvt9W_YYz7ZNN6UZumT0MClnazfF7oGY/edit?usp=sharing",new=2,autoraise=True )


### future tenses


    if event == "future_simple":
        webbrowser.open("https://docs.google.com/spreadsheets/d/1ipHIxokBppXG_BXsVZ02J-HbXtzA5xLLPSm6prZlZ2Q/edit?usp=sharing",new=2,autoraise=True )


    if event == "future_continuous":
        webbrowser.open("https://docs.google.com/spreadsheets/d/1ggv9CToDdZBcjTjDF92r5AYOzAzvFhWZSFuraUdT5mE/edit?usp=sharing",new=2,autoraise=True )

    if event == "future_perfect_continuous":
        webbrowser.open("https://docs.google.com/spreadsheets/d/1ePg18VgsvrrIv1JKcuF6KDTak3jQ46A1ALyv4ElHI5U/edit?usp=sharing",new=2,autoraise=True )

    if event == "future_perfect":
        webbrowser.open("https://docs.google.com/spreadsheets/d/1aq_OhW0JRTGNrowS7Q4RCl52cHx7S9Upha7z9VYp-3o/edit?usp=sharing",new=2,autoraise=True )

    
    if event in ("comparatives and superlatives","comparatives and superlatives1"):
        webbrowser.open("https://docs.google.com/spreadsheets/d/150r972lV3ogmCmlmpjkHNOoX6tIO26Gd4EYzdfCGUW4/edit?usp=sharing",new=2,autoraise=True )


    if event in ("idioms","idioms1"):
        webbrowser.open("https://docs.google.com/spreadsheets/d/15u8oWVJNmjvfkOOvF696E1o-Tz6lBZkr7ctJ6CBLYVk/edit?usp=sharing",new=2,autoraise=True )


    if event in ("prepositional phrases","prepositional phrases1"):
        webbrowser.open("https://docs.google.com/spreadsheets/d/1R3rYYL7H7wC86Z8HeNFy_QzCvqXJSv6w8tKb3wsM30E/edit?usp=sharing",new=2,autoraise=True )

    if event in ("conditionals","conditionals1"):
        webbrowser.open("https://docs.google.com/spreadsheets/d/1VKcLMETbyEnWpVEeXc5j5NjEa_UF0ydMBInS-ljoWhs/edit?usp=sharing",new=2,autoraise=True )


    if event in ("modals","modals1"):
        webbrowser.open("https://docs.google.com/document/d/1KrQamEPrHG4bMQrHc4XJtys-P23iaRC-8iDWXL8sbfY/edit?usp=sharing",new=2,autoraise=True )

    if event in ("question modals","question modals_1"):
        os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/english_questions_modals_and_auxillaries.md"))
        # can trigger multiple events at the same time!
        webbrowser.open("https://docs.google.com/document/d/1KrQamEPrHG4bMQrHc4XJtys-P23iaRC-8iDWXL8sbfY/edit?usp=sharing",new=2,autoraise=True )

       


### timeline events



    if event == "edit timeline events":
                os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/timeline_support_tab/timeline_events.md"))

    if event == "edit adverbs":
                os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/timeline_support_tab/grammar_adverbs_of_time.md"))

    if event == "adverb1":
        with open("/home/dgd/Desktop/python_storyboard_flashcards/timeline_support_tab/grammar_adverbs_of_time.md") as myfile:
            lines = myfile.readlines()
        window["adverb1"].update(random.choice(lines).strip()  )


    if event == "adverb2":
            with open("/home/dgd/Desktop/python_storyboard_flashcards/timeline_support_tab/grammar_adverbs_of_time.md") as myfile:
                lines = myfile.readlines()
            window["adverb2"].update(random.choice(lines).strip()  )


    if event == "adverb3":
            with open("/home/dgd/Desktop/python_storyboard_flashcards/timeline_support_tab/grammar_adverbs_of_time.md") as myfile:
                lines = myfile.readlines()
            window["adverb3"].update(random.choice(lines).strip()  )


    if event == "adverb4":
            with open("/home/dgd/Desktop/python_storyboard_flashcards/timeline_support_tab/grammar_adverbs_of_time.md") as myfile:
                lines = myfile.readlines()
            window["adverb4"].update(random.choice(lines).strip()  )


    if event == "adverb5":
            with open("/home/dgd/Desktop/python_storyboard_flashcards/timeline_support_tab/grammar_adverbs_of_time.md") as myfile:
                lines = myfile.readlines()
            window["adverb5"].update(random.choice(lines).strip()  )


    if event == "adverb6":
            with open("/home/dgd/Desktop/python_storyboard_flashcards/timeline_support_tab/grammar_adverbs_of_time.md") as myfile:
                lines = myfile.readlines()
            window["adverb6"].update(random.choice(lines).strip()  )


    if event == "adverb7":
            with open("/home/dgd/Desktop/python_storyboard_flashcards/timeline_support_tab/grammar_adverbs_of_time.md") as myfile:
                lines = myfile.readlines()
            window["adverb7"].update(random.choice(lines).strip()  )

    if event == "event1":
        with open("/home/dgd/Desktop/python_storyboard_flashcards/timeline_support_tab/timeline_events.md") as myfile:
            lines = myfile.readlines()
        window["event1"].update(random.choice(lines).strip()  )


    if event == "event2":
            with open("/home/dgd/Desktop/python_storyboard_flashcards/timeline_support_tab/timeline_events.md") as myfile:
                lines = myfile.readlines()
            window["event2"].update(random.choice(lines).strip()  )


    if event == "event3":
            with open("/home/dgd/Desktop/python_storyboard_flashcards/timeline_support_tab/timeline_events.md") as myfile:
                lines = myfile.readlines()
            window["event3"].update(random.choice(lines).strip()  )


    if event == "event4":
            with open("/home/dgd/Desktop/python_storyboard_flashcards/timeline_support_tab/timeline_events.md") as myfile:
                lines = myfile.readlines()
            window["event4"].update(random.choice(lines).strip()  )


    if event == "event5":
            with open("/home/dgd/Desktop/python_storyboard_flashcards/timeline_support_tab/timeline_events.md") as myfile:
                lines = myfile.readlines()
            window["event5"].update(random.choice(lines).strip()  )


    if event == "event6":
            with open("/home/dgd/Desktop/python_storyboard_flashcards/timeline_support_tab/timeline_events.md") as myfile:
                lines = myfile.readlines()
            window["event6"].update(random.choice(lines).strip()  )


    if event == "event7":
            with open("/home/dgd/Desktop/python_storyboard_flashcards/timeline_support_tab/timeline_events.md") as myfile:
                lines = myfile.readlines()
            window["event7"].update(random.choice(lines).strip()  )








    if event == "edit prepare_0":
        os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/negotiations_tab/prepare_0.md"))

    if event == "change time":
        now =datetime.date.today().strftime("%Y %B %d %A")
        window["now_event"].update(now)
        #past
        delta1= random.randint(1,370)
        delta2= random.randint(10,300)
        delta3= random.randint(30,390)
        delta4= random.randint(1,370)

        past4 = datetime.date.today()-datetime.timedelta(delta4)
        window["past4"].update(past4.strftime("%Y %B %d %A"))

        past3 = datetime.date.today()-datetime.timedelta(delta1)
        window["past3"].update(past3.strftime("%Y %B %d %A"))
        past2 =  past3 -datetime.timedelta(delta2)
        window["past2"].update(past2.strftime("%Y %B %d %A"))
        past1 =  past2 -datetime.timedelta(delta3)
        window["past1"].update(past1.strftime("%Y %B %d %A"))
        #present
        present1 = datetime.date.today()
        window["present1"].update(present1.strftime("%Y %B %d %A"))

        present2 = datetime.date.today()
        window["present2"].update(present2.strftime("%Y %B %d %A"))

        present3 = datetime.date.today()
        window["present3"].update(present3.strftime("%Y %B %d %A"))


        #future
        delta1= random.randint(1,600)
        delta2= random.randint(10,390)
        delta3= random.randint(30,690)
        delta3= random.randint(30,690)
        future1 =   datetime.date.today()+datetime.timedelta(delta1)
        window["future1"].update(future1.strftime("%Y %B %d %A"))
        future2 =   future1 + datetime.timedelta(delta2)
        window["future2"].update(future2.strftime("%Y %B %d %A"))
        future3 =   future2 + datetime.timedelta(delta3)
        window["future3"].update(future3.strftime("%Y %B %d %A"))
        future4 =   future3 + datetime.timedelta(delta4)
        window["future4"].update(future4.strftime("%Y %B %d %A"))

    if event == "randomize timeline events":
        with open("/home/dgd/Desktop/python_storyboard_flashcards/timeline_support_tab/timeline_events.md") as myfile:
            lines = myfile.readlines()
        random.shuffle(lines)
        # print(lines)
        window["event1"].update(lines[0].strip())
        window["event2"].update(lines[1].strip())
        window["event3"].update(lines[2].strip())
        window["event4"].update(lines[3].strip())
        window["event5"].update(lines[4].strip())
        window["event6"].update(lines[5].strip())
        window["event7"].update(lines[6].strip())

    if event == "randomize adverbs":
        with open("/home/dgd/Desktop/python_storyboard_flashcards/timeline_support_tab/grammar_adverbs_of_time.md") as myfile:
            lines = myfile.readlines()
        random.shuffle(lines)
        window["adverb1"].update(lines[0].strip())
        window["adverb2"].update(lines[1].strip())
        window["adverb3"].update(lines[2].strip())
        window["adverb4"].update(lines[3].strip())
        window["adverb5"].update(lines[4].strip())
        window["adverb6"].update(lines[5].strip())
        window["adverb7"].update(lines[6].strip())




# negotiation events

    if event == "save_negotiation_text_to_md":
        # TODO if fields are empty don't crash
        #prepare_0_list_box
        date_part = "{}.{}.{} {}:{}:{}".format(datetime.date.today().year, 
                    datetime.date.today().month,
                    datetime.date.today().day,
                    datetime.datetime.today().hour,
                    datetime.datetime.today().minute,
                    datetime.datetime.today().second,
                                            )
        print(date_part)
        topic = sg.PopupGetText("topic name",
                                location=(2000, 100),)
        date = sg.PopupGetText("date date",
                                location=(2000, 100),)
        # print("topic name" + topic)
        # print("date" + date_part)
        filename = topic + "_" + date + ".md"
        print(filename)
        text = NEGOTIATION_TEMPLATE.format(values["prepare_0_list_box"],
                                            values["agenda_01_list_box"],
                                            
                                            
                                            )
        #agenda_01_list_box
        with open("/home/dgd/Desktop/python_storyboard_flashcards/negotiations_tab/"+ filename,'w') as myfile:
            myfile.write(text)


##prepare_0
    if event == "prepare0":
            print("event fired")
            with open("/home/dgd/Desktop/python_storyboard_flashcards/negotiations_tab/prepare_0.md") as myfile:
                lines = myfile.readlines()
            window["prepare_0_list_box"].update(random.choice(lines).strip()  )

    

    ###


    ###agenda_01
    if event == "agenda1":
            with open("/home/dgd/Desktop/python_storyboard_flashcards/negotiations_tab/agenda_01.md") as myfile:
                lines = myfile.readlines()
            window["agenda_01_list_box"].update(random.choice(lines).strip()  )
    ###


    ###making_proposals_02
    if event == "proposals2":
            with open("/home/dgd/Desktop/python_storyboard_flashcards/negotiations_tab/making_proposals_02.md") as myfile:
                lines = myfile.readlines()
            window["making_proposals_02_list_box"].update(random.choice(lines).strip()  )
    ###


    ###suggestions_03
    if event == "suggestions3":
            with open("/home/dgd/Desktop/python_storyboard_flashcards/negotiations_tab/suggestions_03.md") as myfile:
                lines = myfile.readlines()
            window["suggestions_03_list_box"].update(random.choice(lines).strip()  )
    ###


    ###agreeing_04
    if event == "agreeing4":
            with open("/home/dgd/Desktop/python_storyboard_flashcards/negotiations_tab/agreeing_04.md") as myfile:
                lines = myfile.readlines()
            window["agreeing_04_list_box"].update(random.choice(lines).strip()  )
    ###


    ###objecting_05
    if event == "objecting5":
            with open("/home/dgd/Desktop/python_storyboard_flashcards/negotiations_tab/objecting_05.md") as myfile:
                lines = myfile.readlines()
            window["objecting_05_list_box"].update(random.choice(lines).strip()  )
    ###


    ###prioritizing_06
    if event == "prioritizing6":
            with open("/home/dgd/Desktop/python_storyboard_flashcards/negotiations_tab/prioritizing_06.md") as myfile:
                lines = myfile.readlines()
            window["prioritizing_06_list_box"].update(random.choice(lines).strip()  )
    ###


    ###clarification_07
    if event == "clarification7":
            with open("/home/dgd/Desktop/python_storyboard_flashcards/negotiations_tab/clarification_07.md") as myfile:
                lines = myfile.readlines()
            window["clarification_07_list_box"].update(random.choice(lines).strip()  )
    ###


    ###compromising_08
    if event == "compromising8":
            with open("/home/dgd/Desktop/python_storyboard_flashcards/negotiations_tab/compromising_08.md") as myfile:
                lines = myfile.readlines()
            window["compromising_08_list_box"].update(random.choice(lines).strip()  )
    ###


    ###bargaining_09
    if event == "bargaining9":
            with open("/home/dgd/Desktop/python_storyboard_flashcards/negotiations_tab/bargaining_09.md") as myfile:
                lines = myfile.readlines()
            window["bargaining_09_list_box"].update(random.choice(lines).strip()  )
    ###


    ###postponing_10
    if event == "postponing10":
            with open("/home/dgd/Desktop/python_storyboard_flashcards/negotiations_tab/postponing_10.md") as myfile:
                lines = myfile.readlines()
            window["postponing_10_list_box"].update(random.choice(lines).strip()  )
    ###


#concluding_11
    if event == "concluding11":
            with open("/home/dgd/Desktop/python_storyboard_flashcards/negotiations_tab/concluding_11.md") as myfile:
                lines = myfile.readlines()
            window["concluding_11_list_box"].update(random.choice(lines).strip()  )
    

###seal_the_deal_12
    if event == "seal_the_deal12":
            with open("/home/dgd/Desktop/python_storyboard_flashcards/negotiations_tab/seal_the_deal_12.md") as myfile:
                lines = myfile.readlines()
            window["seal_the_deal_12_list_box"].update(random.choice(lines).strip()  )

    if event == "edit agenda_01":
                os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/negotiations_tab/agenda_01.md"))
                


    if event == "edit making_proposals_02":
                os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/negotiations_tab/making_proposals_02.md"))
                


    if event == "edit suggestions_03":
                os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/negotiations_tab/suggestions_03.md"))
                


    if event == "edit agreeing_04":
                os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/negotiations_tab/agreeing_04.md"))

    if event == "edit objecting_05":
                os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/negotiations_tab/objecting_05.md"))

    if event == "edit prioritizing_06":
                os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/negotiations_tab/prioritizing_06.md"))

    if event == "edit clarification_07":
                os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/negotiations_tab/clarification_07.md"))

    if event == "edit compromising_08":
                os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/negotiations_tab/compromising_08.md"))
           

    if event == "edit bargaining_09":
                os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/negotiations_tab/bargaining_09.md"))
                

    if event == "edit postponing_10":
                os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/negotiations_tab/postponing_10.md"))
                

    if event == "edit concluding_11":
                os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/negotiations_tab/concluding_11.md"))
                

    if event == "edit seal_the_deal_12":
                os.system("{} {}".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/negotiations_tab/seal_the_deal_12.md"))
                







    if event == sg.WIN_CLOSED or event == "Cancel" or event == 'Exit' :
        break

window.close()
