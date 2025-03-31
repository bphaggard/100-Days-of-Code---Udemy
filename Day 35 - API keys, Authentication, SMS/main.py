import requests

API_KEY = "572e1af2f7ffdb42b2248d45b630b14c"

MY_LAT = 49.195061 # Brno latitude
MY_LONG = 16.606836 # Brno longitude


response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=49.195061&lon=16.606836&appid=572e1af2f7ffdb42b2248d45b630b14c")
response.raise_for_status()
data = response.json()
print(data["cod"])
print(data)
