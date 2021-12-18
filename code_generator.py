#code generator

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

for i in source_list:
    print(f"""  
###
{i}_list = []

###

{i}_list.clear()      

###

with open("negotiations/{i}.md") as myfile:
    for line in myfile.readlines():
        {i}_list.append(line.strip())

### 
[
    sg.Text("{i}"),
    sg.Listbox({i}_list,key="{i}_list_box",enable_events=True,change_submits=True,size=(55,1)),
    sg.Button('shuffle {i}'),
],
###
    
                    """) 



