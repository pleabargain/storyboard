import random 
from datetime import date
from datetime import datetime 

# I want to be able to generate random dates 
# base time is today
# I want random dates in the past
# I want random dates in the future

# i could generate random numbers between x and y and then use those values to generate dates.


# start_date = datetime(2020, 1, 30) 
start_date = datetime(2020, 1, 30) 
future_date = datetime(2022, 5, 28) 
past_date = start_date + (future_date - start_date) * random.random() 

today = date.today()
print("### past date ###\n\n",past_date.strftime("%B %d, %Y"))
# print("today is:\n",today)
print("Today's date:\n\n", today.strftime("%B %d, %Y"))
print("future day:\n\n", future_date.strftime("%B %d %Y"))

random_date = start_date + (future_date - start_date) * random.random() 

# I tried converting today to a string it didn't work
# I need to understand types better
# random_date = start_date + (str(today) - start_date) * random.random() 




# print(random_date)
print("this is a random date:",random_date.strftime("%B %d, %Y"))


