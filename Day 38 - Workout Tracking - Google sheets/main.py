import os
from datetime import datetime
import requests

APP_ID = os.environ.get("APP_ID_NUTRI")
API_KEY = os.environ.get("API_KEY_NUTRI")
SHEET_TOKEN = os.environ.get("SHEET_TOKEN")

GENDER = "male"
WEIGHT_KG = 79
HEIGHT_CM = 178
AGE = 36

user_query = input("Tell me which exercises you did: ")

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
nutri_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

nutri_item = {
    "query": user_query,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=nutritionix_endpoint, json=nutri_item, headers=nutri_headers)
data = response.json()
#print(data)

sheet_endpoint = "https://api.sheety.co/044b63e3ab4b160ae6f78a00cfef289d/workoutTracking/sheet1"

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

sheet_headers = {
    "Authorization": f"Bearer {SHEET_TOKEN}"
}

for exercise in data["exercises"]:
    sheet_inputs = {
        "sheet1": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=sheet_headers)
    print(sheet_response.text)