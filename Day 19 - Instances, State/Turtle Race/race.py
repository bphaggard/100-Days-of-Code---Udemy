from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
colors = ["yellow", "orange", "red", "green", "blue", "purple"]
y_positions = [-80, -40, 0, 40, 80, 120]
all_turtles = []

game_start = False

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-230, y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    game_start = True

while game_start:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            game_start = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The winning turtle was {winning_color}")
            else:
                print(f"You've lost! The winning turtle was {winning_color}")

        random_distance = random.randint(1, 10)
        turtle.forward(random_distance)

screen.exitonclick()