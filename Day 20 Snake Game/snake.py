from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
directions = [0, 90, 180, 270]

class Snake:

    def __init__(self):
        self.segments = []

        for snk in STARTING_POSITIONS:
            snake = Turtle(shape="square")
            snake.color("white")
            snake.penup()
            snake.goto(snk)
            self.segments.append(snake)

        self.head = self.segments[0]

    def move(self):
        for move in range(len(self.segments) - 1, 0, -1): #Reverse order. From last to first (2, 1, 0)
            new_x = self.segments[move - 1].xcor()
            new_y = self.segments[move - 1].ycor()
            self.segments[move].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != directions[3]:
            self.head.setheading(directions[1])

    def down(self):
        if self.head.heading() != directions[1]:
            self.head.setheading(directions[3])

    def left(self):
        if self.head.heading() != directions[0]:
            self.head.setheading(directions[2])

    def right(self):
        if self.head.heading() != directions[2]:
            self.head.setheading(directions[0])