from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.geometry('300x150+100+200')
window.config(padx=30, pady=30)

def button_click():
    entry_value = user_input.get()
    converted_value = round(float(entry_value) * 1.609)
    my_label_4.config(text=str(converted_value))

#Label 1
my_label_1 = Label(text="Miles", font=("Arial", 16))
my_label_1.grid(column=2, row=0)

#Label 2
my_label_2 = Label(text="Km", font=("Arial", 16))
my_label_2.grid(column=2, row=1)

#Label 3
my_label_3 = Label(text="is equal to", font=("Arial", 16))
my_label_3.grid(column=0, row=1)

#Label Result
my_label_4 = Label(text=0, font=("Arial", 16))
my_label_4.grid(column=1, row=1)

#Entry(input)
user_input = Entry(width=7)
user_input.grid(column=1, row=0)

#Button
button = Button(text="Calculate", command=button_click)
button.grid(column=1, row=2)

window.mainloop()