from datetime import datetime

import requests

MY_LAT = 49.195061 # Brno latitude
MY_LONG = 16.606836 # Brno longitude

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0] # output is just hour and not the whole datetime
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)

time_now = datetime.now().hour
print(time_now)