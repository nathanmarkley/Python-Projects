from tkinter import *
from time import *

def get_time():
    timeString = strftime("%H:%M:%S")
    timeLabel.config(text=timeString)

    window.after(1000, get_time)

window = Tk()
window.title("Digital Clock")

timeLabel = Label(window, font=("Arial",100), bg="black", fg="#00FF00")
timeLabel.pack()

get_time()

window.mainloop()