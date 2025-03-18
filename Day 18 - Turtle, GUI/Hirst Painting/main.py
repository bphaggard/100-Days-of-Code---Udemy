import random
import colorgram
import  turtle as t

#Extract RGB colors from image
# colors = colorgram.extract("hirst_dots.jpg", 30)
# color_palette = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     color_palette.append(new_color)

extracted_colors = [(211, 210, 210), (189, 167, 121), (57, 90, 111), (113, 43, 35), (163, 89, 64), (210, 212, 214), (208, 211, 208), (211, 209, 210), (64, 43, 43), (171, 183, 170), (136, 149, 69), (127, 160, 172), (101, 79, 89), (83, 133, 108), (108, 39, 44), (39, 61, 47), (45, 40, 41), (211, 196, 124), (174, 150, 152), (36, 71, 88), (179, 106, 80), (36, 67, 84), (207, 185, 181), (99, 140, 119), (184, 198, 181), (148, 116, 120), (204, 183, 186), (180, 195, 200), (53, 69, 59), (122, 129, 135)]

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
tim.hideturtle()

def start_position():
    tim.penup()
    tim.goto(-200, -200)

def random_color():
    r_color = random.choice(extracted_colors)
    return r_color

def dots_x():
    for move_x in range(10):
        tim.dot(20, random_color())
        tim.penup()
        tim.fd(50)

def dots_y():
    y = -150
    for move_y in range(9):
        tim.penup()
        tim.setposition(-200, y)
        dots_x()
        y += 50

start_position()
dots_x()
dots_y()

screen = t.Screen()
screen.exitonclick()