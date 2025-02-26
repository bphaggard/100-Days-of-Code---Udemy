from tkinter import *

window = Tk()
window.title("My First GUI Program")
#window.minsize(500, 300)
window.geometry('500x300+200+200') #widthxheight+xcor+ycor
window.config(padx=20, pady=20) #Set padding for whole window. Can be also used for specific widget

def button_click():
    entry_val = user_input.get()
    my_label.config(text=entry_val)

#Label
my_label = Label(text="I'm a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

#Changing text
my_label["text"] = "New text"
my_label.config(text="New text 2")

#Button
button = Button(text="Click Me", command=button_click)
button.grid(column=1, row=1)

#Button 2
button = Button(text="New Button", command=button_click)
button.grid(column=2, row=0)

#Entry(input)
user_input = Entry(width=10)
user_input.grid(column=3, row=2)

#Layouts
#pack(), place(), grid(). Use only one of these

window.mainloop()