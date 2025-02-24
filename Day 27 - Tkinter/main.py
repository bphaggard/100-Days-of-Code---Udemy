import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(500, 300)

#Label
my_label = tkinter.Label(text="I'm a Label", font=("Arial", 24, "bold"))
my_label.pack() #this show the label

window.mainloop()