import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0) #works with while loop

game_on = True

right_paddle = Paddle((370, 0))
left_paddle = Paddle((-380, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

while game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.ball_move()

    #Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() <= -280:
        ball.wall_bounce()

    #Detect collision with the right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 340:
        ball.paddle_bounce()


    #Detect collision with the left paddle
    if ball.distance(left_paddle) < 50 and ball.xcor() < -350:
        ball.paddle_bounce()

    #Detect missing the paddle
    if ball.xcor() > 400:
        ball.refresh_game()
        score.increase_left_score()

    if ball.xcor() < -400:
        ball.refresh_game()
        score.increase_right_score()

screen.exitonclick()