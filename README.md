# storyboard
This application will help teachers of English deliver dynamic lessons to their students.

I built it to support my own services. You may use this code as you see fit but I offer ZERO support.

It's a work in progress. I hope it will be useful to others.

The app should run on any python3 compliant device.

# advice
- Do not edit the database manually unless you have to!
- Make frequent back ups!
- Use good naming structures for your variables

# requirements

- python3
- pysimplegui
- see the requirements text


# TODO
There are lots of TODOs in the code. If you want to participate, please do.

- strip empty spaces from files
- sort text files
- strip txt files of empty lines
- set python script to run BASH `cat verbs.txt | sort | uniq>outv.txt` to quickly sort and get uniq values only. )
- add usage license
<img src="/support_images/todo.2021-12-22_10-58.png" alt="todo" />

# DONE
- Save/Load student data from JSON file
  - The json reader is sensitive. If it doesn't find a value on open it will die!
- negotiation tab: randomly chosen text should take focus or find a better way to get text to display
- print full DAY in timeline tab = strftime("%Y %B %d %A")
- automatically generate ten text input fields from a text file source

# list of tabs (not in order)
<img src="/support_images/tabs2022-01-18_13-58.png" alt="Getting started" />

# questions tab
- Display multiple choice questions in the UI.
- flag problem questions
- save student results
- display instructions by category


# grammar tracker tab
- The content in this tab is automatically generated from a text file! It currently saves to file as json. It should load from a student json file. The grammar tracker tab is generated from a text file. The keys for the generated input and sliders should also be generated as well e.g.

if event == "generated key":
   pass

see form_generator_description.md

## TODO
- load data based on date
- create a graph of the student data


## done
- read and write to json file
- save vocabulary data to json file
- create list of adverbs past
- see /grammar_adverbs_of_time.md
# adj noun reg verb tab 
<img src="/support_images/tab_verbadjnoun.png" alt="Getting started" />

You can edit the source files and hit the reload button and the application will load the new files.



# pros and cons tab
This is a great tab for groups as you can get people discussing pros and cons ad nauseum. Think about SCRUM and story point values.

Currently can save the file as csv.

## TODO
Read file from csv.


<img src="/support_images/pros_cons_tab.png" alt="Getting started" />

# tenses tab 
<img src="/support_images/tab_tenses.png" alt="Getting started" />
1. press the shuffle the images button to get random images
   


displays random pictures and the name of the picture

The images are prefixed with adjective, noun, verb etc. The images' prefixes are stripped before loading the image name.

encourage students to make up new sentences

buttons at top go to unique web pages with examples of text


# negotiation tab
<img src="/support_images/tab_negotiations.png" alt="Getting started" />

The idea here is that students will work through a negotiation process using some of the randomly chosen phrases.

All of the items have buttons that will allow you to edit the files in real time.

# timeline tab
## description
This tab generates random dates e.g. SUN December 19th

The dates will be from past to present(now) to future

Random events will be displayed

The teacher instructs the learner to use the time stamp and tell a story with the event.
## todo
- needs to be trimmed down
  - remove unnecessary repetition
  - prompt for input!

## pseudo code for timeline tab
load tab

load timestamp function

prompt user for start date

prompt user for end date

populate date fields
if date_field < NOW 
then 
populate before_now fields

if date_field > NOW
then 
populate after_now fields

# pros and cons tab
- randomly display issue

- get student response for pro and con

- estimate cost of pro and con

- perform analysis of pro and con

- save all values to file (csv? yaml? ?)

- if teacher wants to reload file again in future, file format is tab friendly
- 
## use case 1 pros and cons tab
1. display issue 'get ice cream'
2. student describes pro and con issue of get ice cream
3. teacher records issues
4. T prompts S for analysis
   1. If conditionals
   2. Modal situations
5. save content to file


# 2022 Jan 18
got questions to randomize

cleaned up the UI  a bit

explored SPACY rendering in the question tab UI. Debating if the value of the word is more important than the graph.


# 2022 Jan 14
Trying to get question tab working in development version. Much to do there yet. Thinking hard about what forces are behind creating a web UI. I can't copy and paste working bits to get them working elsewhere. Too much repetition in the code!


# 2022 jan 12


TODO
on save notify user that sentence was saved in adj noun verb tab

TODO clear all text fields contents in pros_cons

---

bug report 

on saving new student grammar track

error

```Traceback (most recent call last):
  File "/home/dgd/Desktop/python_storyboard_flashcards/working.development_python_storyboards.py", line 1628, in <module>
    window["input2"].update(hold_json[most_recent_date]["articles"][0])
KeyError: 'articles'```



# 2022 Jan 6

found my word list folder was missing!

I don't remember if I had pushed my most recent changes to github before ending my day yesterday. 



# 2022 Jan 5
Got the grammar tracker save and load JSON to work. 

It's important to think through the save and load process! All of the save/load code could have been generated at the beginning. 

Test often is also important.

Sensical naming structures is critical e.g. 'input' is just useless when having to refactor!



# bash tip sort
cat verbs.txt | sort | uniq>outv.txt

quickly sort and get uniq values only. 

# bash tip change upper case to lower
tr '[:upper:]' '[:lower:]' < linking_words_reason.txt > output.txt



# language teacher?
Check out the tips page in the app. It's not complete but it'll get your started.


# thanks
Thanks go to Horst Jens who was instrumental in teaching me how to build this application. 