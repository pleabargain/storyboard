# storyboard
This application will help teachers of English deliver dynamic lessons to their students.

I built it to support my own services. You may use this code as you see fit but I offer ZERO support.

# requirements

python3
pysimplegui




# TODO
- negotiation tab: randomly chosen text should take focus or find a better way to get text to display
- add license


# tab adj noun reg verb
<img src="/support_images/tab_verbadjnoun.png" alt="Getting started" />

You can edit the source files and hit the reload button and the application will load the new files.


# tab tenses
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
## descrition
This tab generates random dates e.g. SUN December 19th

The dates will be from past to present(now) to future

Random events will be displayed

The teacher instructs the learner to use the time stamp and tell a story with the event.

## pseudo code
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

## TODO
create list of adverbs past
see /home/dgd/Desktop/EnglishHelpsYourCareer/grammar_adverbs_of_time.md



get random events (not time specific)

e.g.
born
marry
car accident
travel to Africa
employ
dine
marriage
bike trip

# thanks
Thanks go to Horst Jens who was instrumental in teaching me how to build this application. 