import pandas as pa
import datetime as dt
from smtplib import *
from random import randint

email1 = "mail_name1@gmail.com"
password1 = "password"

# email2 = "mail_name2@gmail.com"
#
connection = SMTP("smtp.gmail.com")
# gmail doesn't let less secure apps to access a mail, i guess i'll just understand the logic and move on, i might
# do it with another mail provider sometime later, probably not, being not that into birthdays


# def amount_of_lines(file):
#     with open(file, 'r') as fp:
#         for count, line in enumerate(fp):
#             pass
#         return count


# now = dt.datetime.now()
# now_weekday = now.weekday()
# if now_weekday == 5:
#     random_line = randint(0, amount_of_lines("quotes.txt"))
#     with open("quotes.txt") as text:
#         data = text.readlines()
#         connection.starttls()
#         connection.login(user=email1, password=password1)
#         connection.sendmail(from_addr=email1, to_addrs=email2, msg=f"Happy saturday!\nQOTD: {data[random_line]}")
#         connection.close()

def text(name):  # my guess is this should also work, i didn't want to do the invitation maker solution
    random_number = randint(0, 3)
    if random_number == 0:
        return f"Dear {name}," \
               f"Happy birthday!" \
               f"All the best for the year!" \
               f"E"
    if random_number == 1:
        return f"Hey {name}," \
               f"Happy birthday!" \
               f"Have a wonderful time today and eat lots of cake!" \
               f"Lots of love, E"
    if random_number == 0:
        return f"Dear {name}," \
               f"It's your birthday!" \
               f"Have a great day!" \
               f"All my love," \
               f"E"


bday_data = pa.read_csv("bdays.csv")
now = dt.datetime.now()


connection.starttls()
connection.login(user=email1, password=password1)
number = 0  # this is ridiculous, but it works i guess
for name in bday_data.name.to_list():
    if bday_data.month.to_list()[number] == now.month:
        if bday_data.day.to_list()[number] == now.day:
            print(f"whee its {bday_data.name.to_list[number]} birdday doday")
            connection.sendmail(from_addr=email1, to_addrs=bday_data.mail.to_list()[number], msg=text(bday_data.name.to_list[number]))
    number += 1

# connection.close()
