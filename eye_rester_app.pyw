import tkinter as tk
from tkinter import *
import random
from os.path import dirname


# defining the class - the main application class
class EyeResterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("EYE rester")

        self.countdown_seconds = 20

        # calling methods to load image, create GUI and center the app
        self.load_images()
        self.create_widgets()
        self.center_window()

        # initialize the timer
        self.update_timer()

    # Defining a method, to change background color of the GUI every time it runs
    def color_generator(self):
        self.colors1 = [
            "#856ff8",
            "#46ACC0",
            "#9CD4FE",
            "#78bdf5",
            "#348a4d",
            "#CE6190",
            "#E6B6BB",
            "#CEBC61",
            "#ffc02e",
        ]
        self.colors2 = [
            "#217947",
            "#496757",
            "#991a20",
            "#8D4545",
            "#404ca1",
            "#6e056f",
        ]
        color_set = random.randrange(0, 2, 1)
        if color_set == 1:
            self.bg_color = random.choice(self.colors1)
            self.txt_color = "#000000"
        else:
            self.bg_color = random.choice(self.colors2)
            self.txt_color = "#f8f6e8"

    # method to then trace the location of the images
    def folder_path(self):
        return dirname(__file__)

    # finding the images and calling them
    def load_images(self):
        image_path = str(self.folder_path()) + "/images/option_2--.png"
        image_path = image_path.replace("\\", "/")

        self.image = PhotoImage(file=image_path)

    # Defining a method to create GUI widgets
    def create_widgets(self):
        self.color_generator()

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        self.image_label = tk.Label(self.root, image=self.image)
        self.image_label.pack(
            side=tk.LEFT,
            anchor=tk.NW,
            pady=40,
            padx=(60, 15),
        )
        self.image_label.configure(bg=self.bg_color)

        self.welcome_label = Label(
            self.root,
            text="It's time to give your eyes a rest!\n\nLook ~20 feet away",
            font=(
                "CIN",
                14,
            ),
            anchor=CENTER,
            fg=self.txt_color,
            pady=30,
        )
        self.welcome_label.configure(bg=self.bg_color)
        self.welcome_label.pack()

        self.timer_label = Label(
            self.root, text=f"Time left: {self.countdown_seconds} seconds", anchor=S
        )
        self.timer_label.configure(bg=self.bg_color)
        self.timer_label.pack()

    # definign a method to center the window on every screen
    def center_window(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        app_width = 540
        app_height = 180

        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)

        self.root.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
        self.root.configure(bg=self.bg_color)

    # method for a timer
    def update_timer(self):
        if self.countdown_seconds > 0:
            self.countdown_seconds -= 1
            self.timer_label.config(
                text=f"Time left: {self.countdown_seconds} seconds",
                font=("Optima", 10),
                fg=self.txt_color,
            )
            self.root.after(1000, self.update_timer)
        else:
            self.timer_label.config(text="Time's up!")


# run
if __name__ == "__main__":
    root = tk.Tk()
    app = EyeResterApp(root)
    root.mainloop()
