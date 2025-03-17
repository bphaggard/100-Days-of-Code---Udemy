from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
data = pandas.read_csv("/Users/patrikmlcoch/PycharmProjects/100DaysofCode/Day 31 - Flash Card/data/french_words.csv")
data_dict = data.to_dict(orient="records")
current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(card_image, image=card_front_image)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(card_image, image=card_back_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

#Card
canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="/Users/patrikmlcoch/PycharmProjects/100DaysofCode/Day 31 - Flash Card/images/card_front.png")
card_back_image = PhotoImage(file="/Users/patrikmlcoch/PycharmProjects/100DaysofCode/Day 31 - Flash Card/images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

#Buttons
no_image = PhotoImage(file="/Users/patrikmlcoch/PycharmProjects/100DaysofCode/Day 31 - Flash Card/images/wrong.png")
button_no = Button(image=no_image, highlightthickness=0, borderwidth=0, command=next_card)
button_no.grid(column=0, row=1)

yes_image = PhotoImage(file="/Users/patrikmlcoch/PycharmProjects/100DaysofCode/Day 31 - Flash Card/images/right.png")
button_yes = Button(image=yes_image, highlightthickness=0, borderwidth=0, command=next_card)
button_yes.grid(column=1, row=1)

next_card()

window.mainloop()

