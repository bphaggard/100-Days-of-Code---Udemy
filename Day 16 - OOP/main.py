# # import another_module
# # print(another_module.another_variable)
#
# #TURTLE documentation
# #https://docs.python.org/3/library/turtle.html
# #https://cs111.wellesley.edu/reference/colors
#
# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DarkOliveGreen4") #timmy is Object and color is Method
#
# #Moving
# timmy.forward(100)
# timmy.left(120)
# timmy.forward(100)
# timmy.left(120)
# timmy.forward(100)
# timmy.circle(100)
#
# my_screen = Screen()
# print(my_screen.canvheight) #my_screen is Object and canvheight is an Attribute
# my_screen.exitonclick() #my_screen is Object and exitonclick() is Method

import prettytable

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("City", ["Brno", "Praha", "Kromeriz"])
table.add_column("Population", [398510, 1335000, 28089])
table.add_column("Postal code", ["602 00", "100 00", "767 01"])
table.align = "l"
print(table)