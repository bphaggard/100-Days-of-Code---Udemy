from turtle import Turtle

STARTING_POSITION = (0, 0)

class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.color("white")
        self.setposition(STARTING_POSITION)