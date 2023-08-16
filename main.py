import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage


root = tk.Tk()
root.title("EYE rester")

image = PhotoImage(file="C:/Users/adams/Desktop/python/.vscode/Eye_rester/images/option_2-.png")

image_label = tk.Label(root, image=image)
image_label.pack(side=tk.LEFT, anchor=tk.NW, pady = "20", padx = "20")

app_width = 400
app_height = 100

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
my_label = Label(root, text=f'Width:{screen_width} Height{screen_height}')


w = Label(root, text = 'Its time to give your eyes a rest!', font = "30", anchor = CENTER, bd = "50")
w.pack()



root.mainloop()








# messagebox.showinfo("Eye Rester", "Look around, for 20 seconds")

# messagebox.showwarning("showwarning", "Warning")ss

# messagebox.showerror("showerror", "Error")

# messagebox.askquestion("askquestion", "Are you sure?")

# messagebox.askokcancel("askokcancel", "Want to continue?")

# messagebox.askyesno("askyesno", "Find the value?")

#messagebox.askretrycancel("askretrycancel", "Try again?")