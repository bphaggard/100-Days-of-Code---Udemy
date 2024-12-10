# #Task 1
# user_number = int(input("Write whole number to check for ODD or EVEN: "))
#
# if user_number % 2 == 0:
#     print("Your number is EVEN")
# else:
#     print("Your number is ODD")

# #Task 2
# weight = 85
# height = 1.85
#
# bmi = weight / (height ** 2)
#
# if bmi < 18.5:
#     print("underweight")
# elif 18.5 <= bmi < 25:
#     print("normal weight")
# else:
#     print("overweight")

# #Task 3
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M or L: ")
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# extra_cheese = input("Do you want extra cheese on your pizza? Y or N: ")
# bill = 0
#
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# elif size == "L":
#     bill += 25
# else:
#     print("You typed the wrong size!")
#
# if pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
#
# if extra_cheese == "Y":
#     bill += 1
#
# print(f"Your total price for pizza is {bill}$")

#Project
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."|` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')
print("Welcome to Treasure Island")
print("Your mission is to find the treasure")

end = "GAME OVER"

print("You're at a cross road. Where do you want to go?")
first_direction = input("Type 'left' or 'right'\n").lower()
if first_direction == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    second_direction = input("Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
    if second_direction == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        third_direction = input("One red, one yellow and one blue. Which color do you choose?\n").lower()
        if third_direction == "red":
            print("Burned by fire.")
            print(end)
        elif third_direction == "blue":
            print("Eaten by beasts.")
            print(end)
        elif third_direction == "yellow":
            print("You WIN!")
        else:
            print(end)
    else:
        print("Attacked by trout.")
        print(end)
else:
    print("Fall into a hole.")
    print(end)