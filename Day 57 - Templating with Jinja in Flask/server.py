import datetime
import random

import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)

@app.route("/blog")
def blog():
    response_blog = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    response_blog.raise_for_status()
    blog_data = response_blog.json()
    return render_template("blog.html", posts=blog_data)

if __name__ == "__main__":
    app.run(debug=True)