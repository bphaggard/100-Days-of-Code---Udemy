from turtle import Turtle

START_POSITION = [(-380, -20), (-380, 0), (-380, 20)]
MOVE_DISTANCE = 20

class Paddle:

    def __init__(self):
        self.segment = []
        self.create_paddle()
        self.top = self.segment[0]

    def create_paddle(self):
        for position in START_POSITION:
            paddle = Turtle(shape="square")
            paddle.color("white")
            paddle.penup()
            paddle.goto(position)
            self.segment.append(position)

    def move(self):
        pass