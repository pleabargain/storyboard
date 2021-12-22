#code generator

# sg.Text("prepare"),
#     sg.Listbox(verbs_list,key="verbs_list_box",enable_events=True,change_submits=True,size=(55,1)),
#     sg.Button('shuffle prepare'),
#     ],

source = [
"prepare_0",
"agenda_01",
"making_proposals_02",
"suggestions_03",
"agreeing_04",
"objecting_05",
"prioritizing_06",
"clarification_07",
"compromising_08",
"bargaining_09",
"postponing_10",
"concluding_11",
"seal_the_deal_12",
]

# make sure you test your code

# for i in source:
#     print(f"""[
#     sg.Text("{i}"),
#     sg.Text(
#             text= "Have your prepared enough?!",
#             key="{i}_list_box",
#             enable_events=True,
#             font=("Helvetica", 14),
#             justification = "center",
#             size=(55,1)
#             ),
#     sg.Button('edit {i}'),

# ],
# """)








for i in source:
    print(f"""
###{i}
if event == "{i}_list_box":
        with open("/home/dgd/Desktop/python_storyboard_flashcards/negotiations/{i}.md") as myfile:
            lines = myfile.readlines()
        window["{i}_list_box"].update(random.choice(lines).strip()  )
###
""")


###########












# for i in source_list:
#     print(f"""  
# ###
# {i}_list = []

# ###

# {i}_list.clear()      

# ###

# with open("negotiations/{i}.md") as myfile:
#     for line in myfile.readlines():
#         {i}_list.append(line.strip())

# ### 
# [
#     sg.Text("{i}"),
#     sg.Listbox({i}_list,key="{i}_list_box",enable_events=True,change_submits=True,size=(55,1)),
#     sg.Button('shuffle {i}'),
# ],
# ###
    
#                     """) 
#