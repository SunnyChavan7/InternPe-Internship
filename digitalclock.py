# DIGITAL CLOCK USING PYTHON
from tkinter import *
from time import *

def update():
    time_string = strftime("%I:%M:%S %p") #Convert a time tuple to a string according to a format specification
    time_label.config(text=time_string)

    date_string = strftime("%d %B, %Y")
    date_label.config(text= date_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)


    #time_label.after(1000, update)
    #date_label.after(1000, update)
    #day_label.after(1000, update)
    root.after(1000, update)


root = Tk()

time_label = Label(root, font=("Arial", 100), fg="cyan", bg="black")
time_label.pack(anchor="center")

date_label = Label(root, font=("Baskerville Old Face", 50), fg="black", bg="white")
date_label.pack()

day_label = Label(root, font=("Baskerville Old Face", 40), fg="black", bg="white")
day_label.pack()

update()

root.mainloop()