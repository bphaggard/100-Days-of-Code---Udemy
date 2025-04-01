import requests
import os
from twilio.rest import Client

API_KEY = os.environ.get("OWM_API_KEY")
account_sid = "AC33b6797ac7f5a4bb66d9c041322f72bc"
auth_token = os.environ.get("SMS_TOKEN")

# MY_LAT = 49.195061 # Brno latitude
# MY_LONG = 16.606836 # Brno longitude

# Sulmona
MY_LAT = 42.046829
MY_LONG = 13.925650

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "cnt": 4
}

# Call 5 day / 3 hour forecast data
response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=weather_params)
response.raise_for_status()
data = response.json()
#print(response.status_code)
#print(data["list"][0]["weather"][0]["id"])

weather_codes = [data["list"][index]["weather"][0]["id"] for index in range(0, 4)]
code = any(x <= 700 for x in weather_codes)
if code:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="", # Twilio number
        to="" # My number
    )
    print(message.status)