import tkinter
from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = entry_1.get()
    email = entry_2.get()
    password = entry_3.get()

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
gen_pass = Button(text="Generate Password")
gen_pass.grid(column=2, row=3)

add_pass = Button(text="Add", width=36, command=save_password)
add_pass.grid(column=1, row=4, columnspan=2)

window.mainloop()