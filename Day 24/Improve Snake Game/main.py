import time
from turtle import Screen
from snake import Snake
from scoreboard import Score
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
game_score = Score()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True

while game_on:
    time.sleep(0.1)
    screen.update()
    snake.move()

    #Detect collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 280 or snake.head.ycor() < -290:
        game_score.reset_score()
        snake.reset_snake()

    #Detect collision with the food
    if snake.head.distance(food) < 15:
        game_score.increase_score()
        snake.extend()
        food.refresh_food()

    #Detect collision with the tail
    for segment in snake.segments[1:]: #[1:] pass first segment and starts from second segment
        if snake.head.distance(segment) < 10:
            game_score.reset_score()
            snake.reset_snake()

screen.exitonclick()