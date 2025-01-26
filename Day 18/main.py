import random
from turtle import Turtle, Screen

timmy_turtle = Turtle()
timmy_turtle.shape("turtle")
timmy_turtle.color("DarkOliveGreen4")

#Draw square
# for move in range(4):
#     timmy_turtle.forward(100)
#     timmy_turtle.right(90)

#Draw dashed line
# for move in range(15):
#     timmy_turtle.pendown()
#     timmy_turtle.forward(10)
#     timmy_turtle.penup()
#     timmy_turtle.forward(10)

#Draw different shapes and colors
# colors = ["AntiqueWhite4", "azure4", "blue4", "brown3", "chartreuse2", "DarkOrange", "DeepPink"]
#
# def draw_shape(color, turns):
#     angle = 360 / turns
#     for move in range(turns):
#         timmy_turtle.color(color)
#         timmy_turtle.forward(100)
#         timmy_turtle.right(angle)
#
# for shape in range(3, 10):
#     turtle_color = random.choice(colors)
#     draw_shape(turtle_color, shape)

#Random walk
colors = ["AntiqueWhite4", "azure4", "blue4", "brown3", "chartreuse2", "DarkOrange", "DeepPink", "DarkGoldenrod1", "CadetBlue1", "DarkOrchid1"]

def random_walk():
    directions = [0, 90, 180, 270]
    for move in range(100):
        timmy_turtle.pensize(10)
        timmy_turtle.speed("normal")
        timmy_turtle.forward(30)
        timmy_turtle.pencolor(random.choice(colors))
        timmy_turtle.setheading(random.choice(directions))

random_walk()

screen = Screen()
screen.exitonclick()