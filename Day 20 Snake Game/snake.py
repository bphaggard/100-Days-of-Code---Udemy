from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.segments = []

        for snk in STARTING_POSITIONS:
            snake = Turtle(shape="square")
            snake.color("white")
            snake.penup()
            snake.goto(snk)
            self.segments.append(snake)

    def move(self):
        for move in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[move - 1].xcor()
            new_y = self.segments[move - 1].ycor()
            self.segments[move].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)