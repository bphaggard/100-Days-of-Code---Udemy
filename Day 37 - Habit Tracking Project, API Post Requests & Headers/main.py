import requests

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "kujdfg56er69",
    "username": "patrick89",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Create new account
response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)