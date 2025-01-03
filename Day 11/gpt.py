import random

def blackJack():
    def calculate_score(cards):
        """Calculate the score of a hand, treating Aces as 1 or 11."""
        if sum(cards) == 21 and len(cards) == 2:
            return 21  # Blackjack
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

    def deal_card():
        """Return a random card from the deck."""
        return random.choice([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])

    print("Welcome to Blackjack!")
    while True:
        user_cards = [deal_card(), deal_card()]
        dealer_cards = [deal_card(), deal_card()]
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)

        game_over = False

        while not game_over:
            print(f"\tYour cards: {user_cards}, current score: {user_score}")
            print(f"\tComputer's first card: {dealer_cards[0]}")

            if user_score == 21:
                print("You win with a Blackjack!")
                game_over = True
            elif user_score > 21:
                print("You went over. You lose!")
                game_over = True
            else:
                another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
                if another_card == 'y':
                    user_cards.append(deal_card())
                    user_score = calculate_score(user_cards)
                else:
                    game_over = True

        while dealer_score < 17:
            dealer_cards.append(deal_card())
            dealer_score = calculate_score(dealer_cards)

        print(f"\tYour final hand: {user_cards}, final score: {user_score}")
        print(f"\tComputer's final hand: {dealer_cards}, final score: {dealer_score}")

        if user_score > 21:
            print("You went over. You lose!")
        elif dealer_score > 21 or user_score > dealer_score:
            print("You WIN!")
        elif user_score == dealer_score:
            print("It's a Draw!")
        else:
            print("You Lose!")

        replay = input("Do you want to play again? Type 'y' or 'n': ").lower()
        if replay != 'y':
            print("Thanks for playing!")
            break
blackJack()