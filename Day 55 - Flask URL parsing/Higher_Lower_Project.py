from flask import Flask

app = Flask(__name__)

@app.route("/")
def start_game():
    return '<h1>Guess a number between 0 and 9</h1>'\
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

if __name__ == "__main__":  # with this code you can use PyCharm Run and Stop button instead of flask run command
    # debug mode on is for automatic reloading the server. Do not need to run and stop after each code changes. Show error hints
    app.run(debug=True)