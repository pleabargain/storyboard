#code generator
#TODO for loop for each block of code

# sg.Text("prepare"),
#     sg.Listbox(verbs_list,key="verbs_list_box",enable_events=True,change_submits=True,size=(55,1)),
#     sg.Button('shuffle prepare'),
#     ],

source_list = [
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

# for i in source_list:
#     print(f"""  
# {i}_list = []
# """)

# for i in source_list:
#     print(f"""  
# {i}_list.clear()""")      

# # ###
# for i in source_list:
#     print(f"""  
# with open("negotiations/{i}.md") as myfile:
#     for line in myfile.readlines():
#         {i}_list.append(line.strip())
# """)
# # ### 


# for i in source_list:
#     print(f"""  
# [
#     sg.Text("{i}"),
#     sg.Listbox({i}_list,key="{i}_list_box",enable_events=True,change_submits=True,size=(55,1)),
#     sg.Button('shuffle {i}'),
#     sg.Button('edit {i}'),

# ],
# ###
# """) 


# for i in source_list:
#     print(f"""

# if event == 'shuffle {i}':
#         window["{i}_list_box"].update(set_to_index=random.randint(0,len({i}_list)-1))
# """)


for i in source_list:
    print(f"""

if event == "edit {i}":
            os.system("_ _".format(EXTERNAL_EDITOR, "/home/dgd/Desktop/python_storyboard_flashcards/negotiations/{i}.md"))
            """)