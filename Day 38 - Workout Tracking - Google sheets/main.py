import os

import requests

APP_ID = os.environ.get("APP_ID_NUTRI")
API_KEY = os.environ.get("API_KEY_NUTRI")

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
print(data)