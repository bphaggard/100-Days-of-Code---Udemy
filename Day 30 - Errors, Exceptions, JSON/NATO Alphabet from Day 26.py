import pandas

nato_data_frame = pandas.read_csv("/Users/patrikmlcoch/PycharmProjects/100DaysofCode/Day 26 - List Comprehension/NATO Alphabet/nato_phonetic_alphabet.csv")

"""{"A": "Alfa", "B": "Bravo"}"""
nato_dict = {row.letter:row.code for (index, row) in nato_data_frame.iterrows()}
#print(nato_dict)

# continue_ask = True
# while continue_ask:
#     try:
#         user_input = input("Enter a word: ").upper()
#         code_name_list = [nato_dict[letter] for letter in user_input]
#     except KeyError:
#         print("Sorry, only letters in the alphabet please")
#     else:
#         print(code_name_list)
#         continue_ask = False

#In function
def generate_phonetic():
    try:
        user_input = input("Enter a word: ").upper()
        code_name_list = [nato_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(code_name_list)

generate_phonetic()