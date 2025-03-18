from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 70, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.setposition(-100, 230)
        self.write(f"{self.left_score}", align=ALIGNMENT, font=FONT)
        self.setposition(100, 230)
        self.write(f"{self.right_score}", align=ALIGNMENT, font=FONT)

    def increase_left_score(self):
        self.left_score += 1
        self.update_score()

    def increase_right_score(self):
        self.right_score += 1
        self.update_score()