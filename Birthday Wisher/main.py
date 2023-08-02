from random import choice, randint
import datetime as t
import smtplib
import pandas

MY_MAIL = "koo@koo.com"
MY_PASSWORD = "awiee"
PLACEHOLDER = "[NAME]"

#reading file
people = pandas.read_csv("birthdays.csv")
individuals = {(row.day,row.month):row for (index,row) in people.iterrows()}
#creating data
current_date = t.datetime.now()
today = (current_date.day, current_date.month)

#opening and reading letters
file = f"letter_templates/letter_{randint(1,3)}.txt"
with open(file=file) as all_letters:
    letter = all_letters.read()
    
#comparing dates and generating random letter
if today in individuals:
    name = individuals[today]["name"]
    letter = letter.replace(PLACEHOLDER, name)
    print(letter)
    
else:
    print("No body's birthday")
    

# for rememberace
# with smtplib.SMTP("mail.google.com") as connection:
#     connection.starttls()
#     connection.login(MY_MAIL, MY_PASSWORD)
#     connection.sendmail(MY_MAIL, individuals[today]["email"], f"Subject:Happy Birthday\n\n{final_letter}")
