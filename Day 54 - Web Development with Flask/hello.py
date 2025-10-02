from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

if __name__ == "__main__":  # with this code you can use PyCharm Run and Stop button instead of flask run command
    app.run()