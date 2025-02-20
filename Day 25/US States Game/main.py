import turtle
import pandas

screen = turtle.Screen()
screen.setup(750, 520)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

game_score = 0
game_on = True
data = pandas.read_csv("50_states.csv")
guessed_states = []

def states_final_check():
    missing_states = []
    for item in data["state"]:
        if item not in guessed_states:
            missing_states.append(item)
    new_data = pandas.DataFrame(missing_states)
    new_data.to_csv("missing_states.csv")

while game_on:
    answer_state = screen.textinput(title=f"{game_score}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        states_final_check()
        break
    for state in data["state"]:
        if state == answer_state:
            game_score += 1
            guessed_states.append(answer_state)
            t = turtle.Turtle()
            t.penup()
            t.hideturtle()
            state_guess = data[data.state == answer_state]
            state_x = state_guess["x"].item()
            state_y = state_guess["y"].item()
            t.goto(state_x, state_y)
            t.write(answer_state)
        if game_score == 50:
            game_on = False