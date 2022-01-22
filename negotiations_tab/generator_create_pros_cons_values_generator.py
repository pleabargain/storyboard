# generator
# 'pro1text', 'pro1value'


# for x in range({x},7):
#     print (f"""'pro{x}text','pro{x}value',""",end="")
#     print (f"""'con{x}text','con{x}value',""",end="")

for x in range(1,7):
    print(f"""
    'pro{x}text': values['pros_{x}'] ,
    'pro{x}value': values['slider_pros_{x}'],
    'con{x}text': values['cons_{x}'] ,
    'con{x}value': values['slider_cons_{x}'],""")