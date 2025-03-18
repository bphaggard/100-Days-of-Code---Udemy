from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.setposition(-280, 260)
        self.write(f"Level: {self.score}", font=FONT, align="left")

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.setposition(0, 0)
        self.write(f"GAME OVER", font=FONT, align="center")