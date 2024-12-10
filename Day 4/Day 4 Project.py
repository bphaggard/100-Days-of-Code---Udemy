import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''


paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''


scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = [rock, paper, scissors]
user_choice = int(input("Choose 0 for rock, 1 for paper or 2 for scissors: "))
computer_choice = random.randint(0, len(game) -1)
print(f"User chose: {game[user_choice]}")
print(f"Computer chose: {game[computer_choice]}")

if user_choice == computer_choice:
    print("It's match")
elif user_choice == 0 and computer_choice == 1:
    print("Computer WON")
elif user_choice == 0 and computer_choice == 2:
    print("You WON")
elif user_choice == 1 and computer_choice == 0:
    print("You WON")
elif user_choice == 1 and computer_choice == 2:
    print("Computer WON")
elif user_choice == 2 and computer_choice == 0:
    print("Computer WON")
elif user_choice == 2 and computer_choice == 1:
    print("You WON")