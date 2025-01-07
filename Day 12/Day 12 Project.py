import random

from art import logo

print(logo)
print("""Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.""")

def guess_game():
    attempts = 0
    random_number = random.randint(1, 100)
    correct_input = True
    game_continue = True

    while correct_input:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

        if difficulty == "easy":
            attempts += 10
            print(f"You have {attempts} attempts remaining to guess the number")
            correct_input = False
        elif difficulty == "hard":
            attempts += 5
            print(f"You have {attempts} attempts remaining to guess the number")
            correct_input = False
        else:
            print("Wrong input")

    while game_continue:
        user_number = int(input("Make a guess: "))
        if user_number < random_number:
            print("Too low.")
            attempts -= 1
            print(f"You have {attempts} attempts remaining to guess the number")
        elif user_number > random_number:
            print("Too high.")
            attempts -= 1
            print(f"You have {attempts} attempts remaining to guess the number")
        elif user_number == random_number:
            print(f"You WIN! You guessed the number {random_number}.")
            game_continue = False

        if attempts == 0:
            print(f"You've run out of attempts. The number was {random_number}. You lose.")
            game_continue = False

guess_game()