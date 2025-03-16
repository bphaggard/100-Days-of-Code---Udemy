import json
import random
import pyperclip
from tkinter import *
from tkinter import messagebox

#JSON
"""
WRITE - json.dump()
READ - json.load()
UPDATE - json.update()
"""

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
    website = entry_1.get().title()
    email = entry_2.get()
    password = entry_3.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) < 1 or len(password) < 1:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                #write: json.dump(new_data, data_file, indent=4)
                #read: data = json.load(data_file) -> print(data) it will convert json to dictionary with mode="r"
                #update: it will add new data and will not overwrite
                #reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            entry_1.delete(0, END)
            entry_2.delete(0, END)
            entry_3.delete(0, END)
            entry_1.focus()
            entry_2.insert(0, "example@gmail.com")
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = entry_1.get().title()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#Logo
canvas = Canvas(width=200, height=200, highlightthickness=0)
pass_img = PhotoImage(file="/Users/patrikmlcoch/PycharmProjects/100DaysofCode/Day 29 - Password Manager/logo.png")
canvas.create_image(100, 100, image=pass_img)
canvas.grid(column=1, row=0)

#Website label
label_1 = Label(text="Website:")
label_1.grid(column=0, row=1)

#Website entry
entry_1 = Entry(width=21)
entry_1.focus()
entry_1.grid(column=1, row=1)

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
search_web = Button(text="Search", width=13, command=find_password)
search_web.grid(column=2, row=1)

gen_pass = Button(text="Generate Password", command=pass_generator)
gen_pass.grid(column=2, row=3)

add_pass = Button(text="Add", width=36, command=save_password)
add_pass.grid(column=1, row=4, columnspan=2)

window.mainloop()