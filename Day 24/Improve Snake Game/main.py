from turtle import Screen
from snake import Snake
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
game_score = Score()

game_on = True

while game_on:
    screen.update()

screen.exitonclick()