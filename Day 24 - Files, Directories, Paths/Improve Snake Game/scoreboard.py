from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


def read_high_score():
    with open("data.txt") as file:
        return int(file.read())


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = read_high_score()
        self.color("white")
        self.penup()
        self.setposition(0, 275)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def save_high_score(self):
        with open("data.txt", mode="w") as save:
            return save.write(str(self.score))

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.setposition(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)