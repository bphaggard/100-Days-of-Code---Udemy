import requests
from datetime import datetime

from dateutil.utils import today

USERNAME = "patrick89"
TOKEN = "kujdfg56er69"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# # Create new account
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# # Create graph
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
# graph_config = {
#     "id": GRAPH_ID,
#     "name": "Cycling Graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "sora"
# }

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Add pixel to the graph
today_day = datetime(year=2025, month=4, day=6)
pixel_config = {
    "date": today_day.strftime("%Y%m%d"), # https://www.w3schools.com/python/python_datetime.asp
    "quantity": "30.5"
}

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)