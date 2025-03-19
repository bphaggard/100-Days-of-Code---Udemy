import random
import smtplib
import datetime as dt

my_email = "patrik.mccall@gmail.com"
password = "dwnn dtuu kguf bufr"

with open("quotes.txt") as file:
    content = file.readlines()
    random_quote = random.choice(content)

current_datetime = dt.datetime.now()
day_of_week = current_datetime.weekday()
if day_of_week == 2: #2 = wednesday
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # encrypt the email, secure connection
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Day 32 Challenge 1\n\n{random_quote}")