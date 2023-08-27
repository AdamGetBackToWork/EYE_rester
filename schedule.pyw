import eye_rester_app
import tkinter as tk
import time

sleep_time = 1 * 20


def run_eye_rester():
    root = tk.Tk()
    app = eye_rester_app.EyeResterApp(root)
    root.mainloop()


if __name__ == "__main__":
    while True:
        run_eye_rester()
        time.sleep(sleep_time)
