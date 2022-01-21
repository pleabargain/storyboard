import csv
import sqlite3


INSTRUCTIONS_FILENAME = "/home/dgd/Desktop/EnglishHelpsYourCareer/category_instructions.csv"


con = sqlite3.connect('test_db.db')

#open csv 
#get list of of categories
#create dict
instructions={}

with open(INSTRUCTIONS_FILENAME) as tmp:
        ireader = csv.reader(tmp, delimiter='|', quotechar='"')
        for row in ireader:
            cat, text = row
            instructions[cat] = text

# edit
# write back to the db NOT to the csv

cur = con.cursor()

# cur.execute("""CREATE TABLE questions (fieldnames,fieldnames,)""") 
cur.execute("""CREATE TABLE category (category,instructions)""") 

# populate table
for cat,instr in instructions.items():
    #print(cat, instr)

    cur.execute(f"""INSERT INTO questions VALUES ({cat},{instr})""")

con.commit()
con.close()