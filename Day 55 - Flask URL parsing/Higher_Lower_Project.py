import random
from flask import Flask

app = Flask(__name__)

random_number = random.randint(0, 9)
print(random_number)

@app.route("/")
def start_game():
    return '<h1>Guess a number between 0 and 9</h1>'\
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

@app.route("/<int:number>")
def guess_number(number):
    if number > random_number:
        return '<h1 style="color:SlateBlue">Too high, try again!</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    elif number < random_number:
        return '<h1 style="color:Tomato">Too low, try again!</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    else:
        return '<h1 style="color:MediumSeaGreen">You found me!</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'

if __name__ == "__main__":  # with this code you can use PyCharm Run and Stop button instead of flask run command
    # debug mode on is for automatic reloading the server. Do not need to run and stop after each code changes. Show error hints
    app.run(debug=True)