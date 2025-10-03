from flask import Flask, render_template

app = Flask(__name__)

def make_bold(function):
    def bold_function():
        return '<b>' + function() + '</b>'
    return bold_function

def make_emphasis(function):
    def emphasis_function():
        return '<em>' + function() + '</em>'
    return emphasis_function

def make_underlined(function):
    def underlined_function():
        return '<u>' + function() + '</u>'
    return underlined_function

@app.route("/")
def hello_world():
    return "<img src='https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExZnFja2x4OGx5MngyMTludTJkNTIyOWM2anZqdmt4a2NoYnU4MzZ4byZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/6eilm5p3PxtGLXdhVO/giphy.gif' width=200>"

@app.route("/<name>")
def greet(name):
    return f"Hello {name}"

@app.route("/bye")
@make_underlined
def bye():
    return "Bye"

if __name__ == "__main__":  # with this code you can use PyCharm Run and Stop button instead of flask run command
    # debug mode on is for automatic reloading the server. Do not need to run and stop after each code changes. Show error hints
    app.run(debug=True)