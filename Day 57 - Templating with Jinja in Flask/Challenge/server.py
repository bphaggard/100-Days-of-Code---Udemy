import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    return "Home Page"

@app.route("/guess/<name>")
def guess_page(name):
    response_age = requests.get(f"https://api.agify.io?name={name}")
    response_gender = requests.get(f"https://api.genderize.io?name={name}")
    response_age.raise_for_status()
    response_gender.raise_for_status()
    age_data = response_age.json()["age"]
    gender_data = response_gender.json()["gender"]
    return render_template("index.html", guess=name, age=age_data, gender=gender_data)

if __name__ == "__main__":
    app.run(debug=True)