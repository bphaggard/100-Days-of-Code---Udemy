import requests

API_KEY = ""

# MY_LAT = 49.195061 # Brno latitude
# MY_LONG = 16.606836 # Brno longitude

# Wien
MY_LAT = 48.208176
MY_LONG = 16.373819

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
    print("Bring an umbrella")
