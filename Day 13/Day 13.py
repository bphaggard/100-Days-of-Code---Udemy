# def my_function():
#     for i in range(1, 20): #bug range(1, 21)
#         if i == 20:
#             print("You got it")
#
# my_function()
import random


# import random
#
# dice_numbers = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = random.randint(1, 6) #bug randint(0, 5)
# print(dice_numbers[dice_num])

# year = int(input("What's your year of birth? "))
#
# if 1983 < year <= 1995:
#     print("You are a millennial.")
# elif year >= 1996:
#     print("You are a Gen Z.")

# age = int(input("How old are you? "))
# if age > 18:
#     print("You can drive")
#
# #try-except
# try:
#     age = int(input("How old are you? "))
# except ValueError:
#     print("You have typed in an invalid number. Try again.")
#     age = int(input("How old are you? "))
#
# if age > 18:
#     print(f"You can drive at age {age}")

#Debugger
def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = new_item + item
    b_list.append(new_item) #Not adding items to b_list because of no indentation
    print(b_list)

mutate([1, 2, 3, 5, 8, 13])