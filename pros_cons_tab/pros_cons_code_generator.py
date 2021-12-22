#code generator

# sg.Text("prepare"),
#     sg.Listbox(verbs_list,key="verbs_list_box",enable_events=True,change_submits=True,size=(55,1)),
#     sg.Button('shuffle prepare'),
#     ],

source_list = [

"pros_01",
"pros_02",
"pros_03",
"pros_04",
"pros_05",
"pros_06",
"pros_07",
"cons_01",
"cons_02",
"cons_03",
"cons_04",
"cons_05",
"cons_06",
"cons_07",

]


for x in range(7):
    #inner loops
    print ("[",end="")
    for pk in ("pros", "cons"):
        print(f"""
        sg.Text('{pk}', size =(4, 1)), sg.InputText(key="{pk}_{x}",size=(40,1)), sg.Slider(key= "slider_{pk}_{x}", orientation = "horizontal",size = (6,10),),
        """,end="")
    print("],")






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



