import smtplib
import requests
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# Live Site
url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)
response.raise_for_status()
webpage_data = response.text


soup = BeautifulSoup(webpage_data, "html.parser")
soup_data_price = soup.find(name="span", class_="aok-offscreen").getText()
soup_data_title = soup.find(name="span", id="productTitle").getText().split()
soup_data_title_one_line = "".join(soup_data_title)
item_price = float(soup_data_price.split("$")[1])

#Email Alert
load_dotenv()
smtp_address = os.getenv("SMTP_ADDRESS")
email_address = os.getenv("EMAIL_ADDRESS")
email_password = os.getenv("EMAIL_PASSWORD") # password generated in gmail account

if item_price < 100:
    with smtplib.SMTP(smtp_address) as connection:
        connection.starttls() #encrypt the email, secure connection
        connection.login(user=email_address, password=email_password)
        connection.sendmail(
            from_addr=email_address,
            to_addrs=email_address,
            msg=f"Subject:Amazon Price Alert!\n\n{soup_data_title_one_line}\nCurrent price is: {item_price}\n{url}".encode("utf-8")
        )