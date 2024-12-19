# def life_in_weeks(age):
#     life = 90
#     weeks = 52
#     total = (life - age) * weeks
#     print(f"You have {total} weeks left.")
#
# life_in_weeks(35)

def calculate_love_score(name1, name2):
    name_1 = name1.lower()
    name_2 = name2.lower()

    true_number = 0
    love_number = 0

    for letter_true1 in "true":
        for letter_true2 in name_1:
            if letter_true1 == letter_true2:
                true_number += 1

    for letter_love1 in "love":
        for letter_love2 in name_1:
            if letter_love1 == letter_love2:
                love_number += 1

    for letter_true1 in "true":
        for letter_true2 in name_2:
            if letter_true1 == letter_true2:
                true_number += 1

    for letter_love1 in "love":
        for letter_love2 in name_2:
            if letter_love1 == letter_love2:
                love_number += 1

    print(f"{true_number}{love_number}")

calculate_love_score("Kanye West", "Kim Kardashian")

# # Solution
# def calculate_love_score(name1, name2):
#     combined_names = name1 + name2
#     lower_names = combined_names.lower()
#
#     t = lower_names.count("t")
#     r = lower_names.count("r")
#     u = lower_names.count("u")
#     e = lower_names.count("e")
#     first_digit = t + r + u + e
#
#     l = lower_names.count("l")
#     o = lower_names.count("o")
#     v = lower_names.count("v")
#     e = lower_names.count("e")
#     second_digit = l + o + v + e
#
#     score = int(str(first_digit) + str(second_digit))
#     print(score)
#
#
# calculate_love_score("Kanye West", "Kim Kardashian")