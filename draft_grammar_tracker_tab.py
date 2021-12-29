grammar_tracker_tab= sg.Tab ("grammar tracker", 
        #create button
        [
            #TODO this TEXT object should be a roll down or similar
        [sg.Text("Grammar issues",size=(40,1),
                # key="pros_cons_issues",
                tooltip = "nothing to Click to change this item.",
                enable_events=False,
                font=("helvetica",20)),
                sg.Button("edit common errors file",tooltip="click to open editor")],


        [
        sg.Text('articles_error', size =(4, 1)), sg.InputText(key="articles_error",size=(40,1)), sg.Slider(enable_events=True,key= "slider_articles_error", orientation = "horizontal",size = (6,10),),
        sg.Text('conditionals_error', size =(4, 1)), sg.InputText(key="conditionals_error",size=(40,1)), sg.Slider(enable_events=True,key= "slider_conditionals_error", orientation = "horizontal",size = (6,10),),
        ],
    
        [
        sg.Text('modals', size =(4, 1)), sg.InputText(key="modals_error",size=(40,1)), sg.Slider(enable_events=True,key= "slider_modals_error", orientation = "horizontal",size = (6,10),),
        sg.Text('connecting words', size =(4, 1)), sg.InputText(key="connecting_words_error",size=(40,1)), sg.Slider(enable_events=True,key= "slider_connecting_words", orientation = "horizontal",size = (6,10),),
        ],
        
        [
        sg.Text('passive voice', size =(4, 1)), sg.InputText(key="passive_voice_error",size=(40,1)), sg.Slider(enable_events=True,key= "slider_passive_voice", orientation = "horizontal",size = (6,10),),
        sg.Text('prepositions', size =(4, 1)), sg.InputText(key="prepositions_error",size=(40,1)), sg.Slider(enable_events=True,key= "slider_prepositions", orientation = "horizontal",size = (6,10),),
        ],

        [
        sg.Text('comparatives and superlatives', size =(4, 1)), sg.InputText(key="comparatives_and_superlatives_error",size=(40,1)), sg.Slider(enable_events=True,key= "slider_comparatives_and_superlatives", orientation = "horizontal",size = (6,10),),
        sg.Text('cons', size =(4, 1)), sg.InputText(key="cons_3",size=(40,1)), sg.Slider(enable_events=True,key= "slider_cons_3", orientation = "horizontal",size = (6,10),),
        ],

        [
        sg.Text('phrasal verbs', size =(4, 1)), sg.InputText(key="phrasal_verbs_error",size=(40,1)), sg.Slider(enable_events=True,key= "slider_phrasal_verbs", orientation = "horizontal",size = (6,10),),
        sg.Text('irregular verbs', size =(4, 1)), sg.InputText(key="irregular_verbs_error",size=(40,1)), sg.Slider(enable_events=True,key= "slider_irregular_verbs", orientation = "horizontal",size = (6,10),),
        ],
        [
        sg.Text('pronunciation', size =(4, 1)), sg.InputText(key="pronunciation_error",size=(40,1)), sg.Slider(enable_events=True,key= "slider_pronunciation_error", orientation = "horizontal",size = (6,10),),
        sg.Text('questions', size =(4, 1)), sg.InputText(key="questions_error",size=(40,1)), sg.Slider(enable_events=True,key= "slider_questions", orientation = "horizontal",size = (6,10),),
        ],
        # [
        # sg.Text('pros', size =(4, 1)), sg.InputText(key="pros_6",size=(40,1)), sg.Slider(enable_events=True,key= "slider_pros_6", orientation = "horizontal",size = (6,10),),
        
        # sg.Text('cons', size =(4, 1)), sg.InputText(key="cons_6",size=(40,1)), sg.Slider(enable_events=True,key= "slider_cons_6", orientation = "horizontal",size = (6,10),),
        # ],

### summary of slider
        [
        sg.Text("performance sum",justification="right", size=(10,1)), sg.Text("?",key="performance sum"),
        ],

### analysis
        [sg.Multiline(key="grammar analysis",size =(40,5),tooltip="This is a multiline on line 983 of the code",font =("helvetica", 14)), sg.Button("save grammar analysis to CSV",tooltip="TODO add student name to file save")],
   

    ])

