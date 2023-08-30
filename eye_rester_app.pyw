import tkinter as tk
from tkinter import *
import time
import random


class EyeResterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("EYE rester")

        self.countdown_seconds = 20

        self.load_images()
        self.create_widgets()
        self.center_window()

        self.update_timer()

    def color_generator(self):
        self.colors = [
            "#856ff8",
            "#46ACC0",
            "#9CD4FE",
            "#31F1FE",
            "#23C06C",
            "#217947",
            "#CE6190",
            "#E6B6BB",
            "#CEBC61",
            "#8D4545",
        ]
        self.bg_color = random.choice(self.colors)

    def load_images(self):
        self.image = PhotoImage(
            file="C:/Users/adams/Desktop/python/.vscode/Eye_rester/images/option_2--.png"
        )

    def create_widgets(self):
        self.color_generator()

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        self.image_label = tk.Label(self.root, image=self.image)
        self.image_label.pack(
            side=tk.LEFT,
            anchor=tk.NW,
            pady=(screen_height / 20),
            padx=(screen_width / 30),
        )
        self.image_label.configure(bg=self.bg_color)

        self.welcome_label = Label(
            self.root,
            text="It's time to give your eyes a rest!\n\nLook ~10 meters away",
            font="30",
            anchor=CENTER,
            pady=(screen_height / 28),
        )
        self.welcome_label.configure(bg=self.bg_color)
        self.welcome_label.pack()

        self.timer_label = Label(
            self.root, text=f"Time left: {self.countdown_seconds} seconds", anchor=S
        )
        self.timer_label.configure(bg=self.bg_color)
        self.timer_label.pack()

    def center_window(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        app_width = int(screen_width / 3.5)
        app_height = int(screen_height / 6)

        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)

        self.root.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
        self.root.configure(bg=self.bg_color)

    def update_timer(self):
        if self.countdown_seconds > 0:
            self.countdown_seconds -= 1
            self.timer_label.config(text=f"Time left: {self.countdown_seconds} seconds")
            self.root.after(1000, self.update_timer)
        else:
            self.timer_label.config(text="Time's up!")


if __name__ == "__main__":
    root = tk.Tk()
    app = EyeResterApp(root)
    root.mainloop()
