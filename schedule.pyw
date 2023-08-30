import eye_rester_app
import tkinter as tk
import time

# sleep time is the time program awaits to initialize (in seconds, thats why * 60)
sleep_time = 20 * 60


# function for calling the app
def run_eye_rester():
    root = tk.Tk()
    app = eye_rester_app.EyeResterApp(root)
    root.mainloop()


# condition for the app to run infinitely
if __name__ == "__main__":
    while True:
        time.sleep(sleep_time)
        run_eye_rester()
