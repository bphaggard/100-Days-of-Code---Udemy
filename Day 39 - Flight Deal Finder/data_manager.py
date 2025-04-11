import os
import requests

SHEET_ENDPOINT = "https://api.sheety.co/044b63e3ab4b160ae6f78a00cfef289d/flightDealFinder/sheet1"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheet_token = os.environ.get("SHEET_FLIGHT_TOKEN")
        self.sheet_headers = {
            "Authorization": f"Bearer {self.sheet_token}"
        }
        self.destination_data = {}

    def get_destination_data(self):
        sheet_response = requests.get(url=SHEET_ENDPOINT, headers=self.sheet_headers)
        sheet_data = sheet_response.json()
        self.destination_data = sheet_data["sheet1"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "sheet1": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEET_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=self.sheet_headers
            )
            print(response.text)