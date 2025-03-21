##################### Normal Starting Project ######################

# HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv that is formated like this:
# birthdays_dict = {
#     (birthday_month, birthday_day): data_row
# }
#Dictionary comprehension template for pandas DataFrame looks like this:
# new_dict = {new_key: new_value for (index, data_row) in data.iterrows()}
#e.g. if the birthdays.csv looked like this:
# name,email,year,month,day
# Angela,angela@email.com,1995,12,24
#Then the birthdays_dict should look like this:
# birthdays_dict = {
#     (12, 24): Angela,angela@email.com,1995,12,24
# }

#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT 1: Think about the relative file path to open each letter.
# HINT 2: Use the random module to get a number between 1-3 to pick a random letter.
# HINT 3: Use the replace() method to replace [NAME] with the actual name. https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.

import random
import smtplib
import datetime as dt
import pandas

my_email = "patrik.mccall@gmail.com"
password = "dwnn dtuu kguf bufr"

current_datetime = dt.datetime.now()
current_date = (current_datetime.month, current_datetime.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {}

# Iterate through each row in the DataFrame
for _, row in data.iterrows():
    month, day = int(row['month']), int(row['day'])
    birthdays_dict[(month, day)] = row.tolist()
# Output the dictionary
#print(birthdays_dict)

# random_number = random.randint(1, 3)
#
# if current_date in birthdays_dict:
#     name = birthdays_dict[current_date][0]
#     with open(f"letter_templates/letter_{random_number}.txt") as letter_file:
#         letter_content = letter_file.read()
#         new_text = letter_content.replace("[NAME]", name)
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls() #encrypt the email, secure connection
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs=my_email,
#         msg=f"Subject:Happy Birthday\n\n{new_text}")