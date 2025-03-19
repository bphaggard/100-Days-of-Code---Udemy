import smtplib

my_email = "patrik.mccall@gmail.com"
password = "dwnn dtuu kguf bufr"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls() #encrypt the email, secure connection
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=my_email,
        msg="Subject:Test Python\n\nHello from PyCharm")

