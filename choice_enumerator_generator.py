#gen py

for i in range(1,11):
    print(f"""if event == "db_choice{i}":
        window["student_question_choice"].update(window["db_choice{i}"].DisplayText)""")

