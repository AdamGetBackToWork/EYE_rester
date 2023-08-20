import tkinter as tk
from tkinter import *
import time


root = tk.Tk()
root.title("EYE rester")

image = PhotoImage(
    file="C:/Users/adams/Desktop/python/.vscode/Eye_rester/images/option_2-.png"
)

image_label = tk.Label(root, image=image)
image_label.pack(side=tk.LEFT, anchor=tk.NW, pady="40", padx="40")

app_width = 400
app_height = 150

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

root.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
my_label = Label(root, text=f"Width:{screen_width} Height{screen_height}")


w = Label(
    root,
    text="Its time to give your eyes a rest! \n \n Look ~20 meters away",
    font="30",
    anchor=CENTER,
    pady="30",
)
w.pack()


countdown_seconds = 20
timer_label = Label(root, text=f"Time left: {countdown_seconds} seconds", anchor=S)
timer_label.pack()


def update_timer():
    global countdown_seconds
    if countdown_seconds > 0:
        countdown_seconds -= 1
        timer_label.config(text=f"Time left: {countdown_seconds} seconds")
        root.after(1000, update_timer)
    else:
        timer_label.config(text="Time's up!")


update_timer()


root.mainloop()
