import random
import hangman_words #or from hangman_words import word_list
import hangman_art

stages = hangman_art.stages
word_list = hangman_words.word_list #if we use from hangman_words import word_list, we don't need this variable
random_word = random.choice(word_list)

print(hangman_art.logo)
print(random_word)
hidden_word = ""

for word in random_word:
    hidden_word += "_"

print(f"Word to guess: {hidden_word}")

game_over = False
correct_letters = []
lives = 6

while not game_over:
    print(f"******************** {lives} LIVES LEFT ********************")
    user_letter = input("Guess the letter from word: ").lower()

    if user_letter in correct_letters:
        print(f"You've already guessed {user_letter}")

    guessed_word = ""

    for letter in random_word:
        if letter == user_letter:
            guessed_word += letter
            correct_letters.append(user_letter)
        elif letter in correct_letters:
            guessed_word += letter
        else:
            guessed_word += "_"

    print(f"Word to guess: {guessed_word}")

    if user_letter not in random_word:
        lives -= 1
        print(f"You guessed {user_letter}, that's not in the word. You lose a life.")

    print(stages[lives])

    if "_" not in guessed_word:
        game_over = True
        print("******************** You WON ********************")

    if lives == 0:
        game_over = True
        print("******************** You Lost ********************")
        print(f"Guessed word was {random_word}")