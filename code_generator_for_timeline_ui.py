# code generator for timeline ui

source = ['one', 'two', 'three', 'four',

]


for i in source:
    print(f"""
timeline_column_{i} = sg.Column([
                                [sg.Text("timeline column {i}",
                                key="timeline column {i}",
                                enable_events=True,
                                tooltip='This is a tool tip timeline column {i}')],


                                ])

""")