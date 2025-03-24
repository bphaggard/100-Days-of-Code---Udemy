import requests

response = requests.get("http://api.open-notify.org/iss-now.json")
# print(response) # returns HTTP status
# print(response.json()) # returns JSON format
# print(response.raise_for_status()) # show type of error for each status code

# HTTP status codes: https://www.webfx.com/web-development/glossary/http-status-codes/

data = response.json()
print(data["iss_position"])