import  turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

directions = [0, 90, 180, 270]

#Spirograph
for move in range(int(360 / 6)):
    tim.color(random_color())
    tim.speed("fastest")
    tim.circle(80)
    tim.left(6)

screen = t.Screen()
screen.exitonclick()