# storyboard
This application will help teachers of English deliver dynamic lessons to their students.

I built it to support my own services. You may use this code as you see fit but I offer ZERO support.

It's a work in progress. I hope it will be useful to others.

The app should run on any python3 compliant device.

# requirements

- python3
- pysimplegui



# TODO
- set python script to run BASH `cat verbs.txt | sort | uniq>outv.txt` to quickly sort and get uniq values only. )
- strip txt files of empty lines
- Save/Load student data from JSON file
- there are lots of TODOs in the code. If you want to participate, please do.
- add usage license
<img src="/support_images/todo.2021-12-22_10-58.png" alt="todo" />

# DONE
- negotiation tab: randomly chosen text should take focus or find a better way to get text to display
- print full DAY in timeline tab = strftime("%Y %B %d %A")
- automatically generate ten text input fields from a text file source

# list of tabs (not in order)
<img src="/support_images/tabs_22dec.png" alt="Getting started" />

# grammar tracker tab
This is automatically generated from a text file! It currently saves to file as json partially. It should load from json eventually but it doesn't yet. The grammar tracker tab is generated from a text file. The keys for the generated input and sliders should also be generated as well e.g.

if event == "generated key":
   pass

## TODO
Read and write to json file

# adj noun reg verb tab 
<img src="/support_images/tab_verbadjnoun.png" alt="Getting started" />

You can edit the source files and hit the reload button and the application will load the new files.



# pros and cons tab
This is a great tab for groups as you can get people discussing pros and cons ad nauseum. Think about SCRUM and story point values.

Currently can save the file as csv.

## TODO
Read and write file to json.
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






## done
- create list of adverbs past
- see /grammar_adverbs_of_time.md

# 2022 Jan 6
found my word list folder was missing!

I don't remember if I had pushed my most recent changes to github before ending my day yesterday. 



# 2022 Jan 5
Got the grammar tracker save and load JSON to work. 

It's important to think through the save and load process! All of the save/load code could have been generated at the beginning. 

Test often is also important.

Sensical naming structures is critical e.g. 'input' is just useless when having to refactor!


# bash tip
cat verbs.txt | sort | uniq>outv.txt

quickly sort and get uniq values only. 

# language teacher?
Check out the tips page in the app. It's not complete but it'll get your started.


# thanks
Thanks go to Horst Jens who was instrumental in teaching me how to build this application. 