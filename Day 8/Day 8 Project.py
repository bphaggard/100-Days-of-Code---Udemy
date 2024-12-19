from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
user_continue = True

print(logo)

def caesar(user_direction, original_text, shift_amount):
    def encrypt():
        encoded_text = ""
        for letter in original_text:
            index_old = alphabet.index(letter) + shift_amount
            if index_old < 25:
                new_letter = alphabet[index_old]
                encoded_text += new_letter
            elif index_old > 25:
                new_letter = alphabet[index_old - 26]
                encoded_text += new_letter
        print(f"Here is the encoded result: {encoded_text}")

    def decrypt():
        decoded_text = ""
        for letter in original_text:
            index_old = alphabet.index(letter) - shift_amount
            new_letter = alphabet[index_old]
            decoded_text += new_letter
        print(f"Here is the decoded result: {decoded_text}")

    if user_direction == "encode":
        encrypt()
    elif user_direction == "decode":
        decrypt()
    else:
        print("You typed wrong direction!")

while user_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(direction, text, shift)

    restart = input("Type 'yes' if you want to go again or 'no' to quit: \n").lower()

    if restart == "no":
        user_continue = False
        print("Goodbye")

# #Solution
# def caesar(original_text, shift_amount, encode_or_decode):
#     output_text = ""
#     for letter in original_text:
#         if letter not in alphabet:
#             output_text += letter
#         else:
#             if encode_or_decode == "decode":
#                 shift_amount *= -1
#
#             shifted_position = alphabet.index(letter) + shift_amount
#             shifted_position %= len(alphabet)
#             output_text += alphabet[shifted_position]
#     print(f"Here is the {encode_or_decode}d result: {output_text}")
#
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
#
# caesar(text, shift, direction)