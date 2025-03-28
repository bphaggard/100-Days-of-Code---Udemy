import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}

trivia_data = requests.get(url="https://opentdb.com/api.php", params=parameters)
trivia_data.raise_for_status()
trivia_json = trivia_data.json()
question_data = trivia_json["results"]