import random
from art import logo, vs
from game_data import data


def random_index():
    """Selects a random entry from the data."""
    return random.choice(data)


def print_comparison(a, b):
    """Prints the comparison details for A and B."""
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
    print(vs)
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}")


def get_winner(a, b):
    """Returns 'A' if A has more followers, otherwise 'B'."""
    return 'A' if a['follower_count'] > b['follower_count'] else 'B'


# Start of the game
print(logo)

score = 0
game_continue = True
compare_a = random_index()
compare_b = random_index()

# Ensure compare_b is not the same as compare_a initially
while compare_b == compare_a:
    compare_b = random_index()

while game_continue:
    # Display the options
    print_comparison(compare_a, compare_b)

    # Get user input
    user_choice = input("Who has more followers on Instagram? Type 'A' or 'B': ").upper()

    # Determine the winner
    winner = get_winner(compare_a, compare_b)

    if user_choice == winner:
        score += 1
        print(f"You're right! Current score: {score}")

        # Update comparison
        if winner == 'B':
            compare_a = compare_b
        compare_b = random_index()

        # Ensure compare_b is not the same as compare_a
        while compare_b == compare_a:
            compare_b = random_index()
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_continue = False
