import random
import pyperclip
from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['%', '#', '$', '!', '&', '(', ')', '*', '+', '?']

    pass_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    pass_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    pass_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list = pass_letters + pass_numbers + pass_symbols
    shuffled_pass = ''.join(random.sample(password_list, len(password_list)))
    entry_3.delete(0, END)
    entry_3.insert(0, shuffled_pass)
    pyperclip.copy(shuffled_pass)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = entry_1.get()
    email = entry_2.get()
    password = entry_3.get()

    if len(website) < 1 or len(password) < 1:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nWebsite: {website} \nEmail: {email} \nPassword: {password}")

        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"{website} | {email} | {password}\n")

            entry_1.delete(0, END)
            entry_2.delete(0, END)
            entry_3.delete(0, END)
            entry_1.focus()
            entry_2.insert(0, "example@gmail.com")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#Logo
canvas = Canvas(width=200, height=200, highlightthickness=0)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_img)
canvas.grid(column=1, row=0)

#Website label
label_1 = Label(text="Website:")
label_1.grid(column=0, row=1)

#Website entry
entry_1 = Entry(width=38)
entry_1.focus()
entry_1.grid(column=1, row=1, columnspan=2)

#Email/Username label
label_2 = Label(text="Email/Username:")
label_2.grid(column=0, row=2)

#Email entry
entry_2 = Entry(width=38)
entry_2.insert(0, "example@gmail.com")
entry_2.grid(column=1, row=2, columnspan=2)

#Password label
label_3 = Label(text="Password:")
label_3.grid(column=0, row=3)

#Password entry
entry_3 = Entry(width=21)
entry_3.grid(column=1, row=3)

#Buttons
gen_pass = Button(text="Generate Password", command=pass_generator)
gen_pass.grid(column=2, row=3)

add_pass = Button(text="Add", width=36, command=save_password)
add_pass.grid(column=1, row=4, columnspan=2)

window.mainloop()