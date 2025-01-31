import time
from turtle import Turtle, Screen

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
positions = [(-40, 0), (-20, 0), (0, 0)]
segments = []

for snk in positions:
    snake = Turtle(shape="square")
    snake.color("white")
    snake.penup()
    snake.goto(snk)
    segments.append(snake)

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    for move in range(len(positions) - 1, 0, -1):
        new_x = segments[move - 1].xcor()
        new_y = segments[move - 1].ycor()
        segments[move].goto(new_x, new_y)
    segments[0].forward(20)

screen.exitonclick()