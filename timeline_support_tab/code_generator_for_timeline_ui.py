# code generator for timeline ui

# source = ['one', 'two', 'three', 'four',

# ]


# for i in source:
#     print(f"""
# timeline_column_{i} = sg.Column([
#                                 [sg.Text("timeline column {i}",
#                                 key="timeline column {i}",
#                                 enable_events=True,
#                                 tooltip='This is a tool tip timeline column {i}')],


#                                 ])

# """)

# source = ["adverb1", "adverb2","adverb3","adverb4", "adverb5","adverb6", "adverb7"]

source = ["event1", "event2", "event3", "event4", "event5", "event6", "event7"]


for i in source:
    print(f"""
if event == "{i}":
        with open("/home/dgd/Desktop/python_storyboard_flashcards/timeline_support/timeline_events.md") as myfile:
            lines = myfile.readlines()
        window["{i}"].update(random.choice(lines).strip()  )
""")
