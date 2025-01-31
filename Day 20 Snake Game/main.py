import time
from turtle import Screen
from snake import Snake

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) #Turtle animation off

game_on = True

snake = Snake()

while game_on:
    screen.update() #Smooth turtle move
    time.sleep(0.1)
    snake.move()

screen.exitonclick()