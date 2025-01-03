import random

from game_art import logo

def deal_card():
    """Return a random number from cards list"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card


def calculate_score(cards):
    """Calculate sum of cards and check for Blackjack"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, dealer_score):
    if user_score == dealer_score:
        return "Draw"
    elif dealer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif dealer_score > 21:
        return "Opponent went over. You Win"
    elif user_score > dealer_score:
        return "You Win"
    else:
        return "You lose"

def blackJack():
    print(logo)
    continue_game = True
    user_cards = [deal_card(), deal_card()]
    dealer_cards = [deal_card(), deal_card()]
    user_cards_sum = -1
    dealer_cards_sum = -1

    while continue_game:
        user_cards_sum = calculate_score(user_cards)
        dealer_cards_sum = calculate_score(dealer_cards)
        print(f"\tYour cards: {user_cards}, current score: {user_cards_sum}")
        print(f"\tComputer's first card: {dealer_cards[0]}")

        if user_cards_sum == 0 or dealer_cards_sum == 0 or user_cards_sum > 21:
            continue_game = False
        else:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

            if another_card == "y":
                user_cards.append(deal_card())
            else:
                continue_game = False

    while dealer_cards_sum != 0 and dealer_cards_sum < 17:
        dealer_cards.append(deal_card())
        dealer_cards_sum = calculate_score(dealer_cards)

    print(f"\tYour final hand: {user_cards}, final score: {user_cards_sum}")
    print(f"\tComputer's final hand: {dealer_cards}, final score: {dealer_cards_sum}")
    print(compare(user_cards_sum, dealer_cards_sum))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    print("\n" * 20)
    blackJack()