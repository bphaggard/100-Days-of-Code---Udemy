import random

from art import logo, vs
from game_data import data

score = 0
game_continue = True

def random_index():
    random_select_index = random.randint(0, len(data) - 1)
    return data[random_select_index]

print(logo)

compare_a = random_index()
compare_b = random_index()

if compare_a == compare_b:
    compare_b = random_index()

while game_continue:
    print(f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}")
    print(vs)
    print(f"Against B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}")
    followers = input("Who has more followers on Instagram? Type 'A' or 'B': ").upper()
    if compare_a["follower_count"] > compare_b["follower_count"]:
        if followers == "A":
            score += 1
            print(f"You're right! Current score: {score}")
            compare_b = random_index()
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_continue = False

    if compare_a["follower_count"] < compare_b["follower_count"]:
        if followers == "B":
            score += 1
            print(f"You're right! Current score: {score}")
            compare_a = compare_b
            compare_b = random_index()
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_continue = False
