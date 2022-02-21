# read pro-con csv and makes pretty html out of it

import csv


# CSVPATH = "go to bed late.csv"
CSVPATH = "/home/dgd/Desktop/python_storyboard_flashcards/pros_cons_tab/move to Wroclaw.csv"
#fields = ["topic",
#          "analysis",
#          "pro0text","pro0value","con0text","con0value","pro1text","pro1value","con1text","con1value","pro2text","pro2value","con2text",
#          "con2value","pro3text","pro3value","con3text","con3value","pro4text","pro4value","con4text","con4value","pro5text","pro5value",
#          "con5text","con5value","pro6text","pro6value","con6text","con6value",
#          ]

# DictReader does not need fieldnames, can get them from first row
with open(CSVPATH) as mycsv:
    reader = csv.DictReader(mycsv)
    for line_number, row in enumerate(reader,start=1):
        #print("line_numer:", line_number, row)
        #print()
        pass # necessary, because the whole loop must run through

#print("-------------")
#print(row) # this is the last line of the csv, already transformed into a dictionary

out = "<h3>pros and cons of: {}</h3>".format(row["topic"])
if row["analysis"].strip() != "":
    out += "analysis: " + '<span style="font-style: italic;">' + row["analysis"] + "</span><br><br>"
out += "<table><tr><th>pro-argument</th><th>&#128077;</th><th>pro</th><th>result</th><th>con</th><th>&#128078;</th><th>con-argument</th></tr>"
pro_score = 0
con_score = 0
for i in range(7):
    protext = row[f"pro{i}text"]
    provalue = float(row[f"pro{i}value"])
    context = row[f"con{i}text"] 
    convalue = float(row[f"con{i}value"])
    print("for-loop:", i, protext, provalue, context, convalue)
    if (protext.strip() != "") or ( context.strip() != ""):
        pro_score += provalue
        con_score += convalue
        tmp = '<tr><td style="text-align:left;">{}</td><td style="text-align:right;">{}</td><td style="text-align:right;">{}</td>'
        tmp += '<td style="text-align:center;"> {} </td>'
        tmp +='<td style="text-align:right;">{}</td><td style="text-align:left;">{}</td><td style="text-align:right;">{}</td>'
        tmp += '</tr>'
        tmp = tmp.format(protext, 
                        int(provalue) * "&#128077;",    # thumb up
                        provalue,
                        "&#128528;" if provalue == convalue else " &#128533;" if provalue < convalue else "&#128578;",
                        # neutral face: &#128528;  smiling face: &#128578;   confused (sad) face: &#128533;
                        convalue,
                        int(convalue) * "&#128078;",    # thumb down
                        context )
        out += tmp
tmp = '<tr"><td style="text-align:left;border-top: 2px solid #000000;">summary:</td>'
tmp +='<td></td><td style="text-align:right;border-top: 2px solid #000000;">{}</td>'
tmp +='<td style="text-align:center;border-top: 2px solid #000000;">{}</td>'
tmp +='<td style="text-align:right;border-top: 2px solid #000000;">{}</td><td></td><td></td></tr>'
tmp = tmp.format(pro_score,
                 "&#128528;" if pro_score == con_score else " &#128533;" if pro_score < con_score else "&#128578;", 
                 con_score   )
out += tmp
out += "</table>"

with open("output.html", "w") as htmlfile:  
    htmlfile.write(out)
print("done")
        
