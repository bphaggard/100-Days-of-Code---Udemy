from tkinter import *

window = Tk()
window.title("My First GUI Program")
#window.minsize(500, 300)
window.geometry('500x300+200+200') #widthxheight+xcor+ycor

#Label
my_label = Label(text="I'm a Label", font=("Arial", 24, "bold"))
my_label.pack() #this show the label

#Changing text
my_label["text"] = "New text"
my_label.config(text="New text 2")

#Button
def button_click():
    entry_val = user_input.get()
    my_label.config(text=entry_val)

button = Button(text="Click Me", command=button_click)
button.pack()

#Entry(input)

user_input = Entry(width=10)
user_input.pack()

window.mainloop()