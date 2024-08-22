import datetime
import schedule
import time
import tkinter as tk
from tkinter import messagebox


class Application:

    def __init__(self):
        # Define your workout schedule
        self.workout_schedule = {
            "Monday": "Pull Day (Back)",
            "Tuesday": "Biceps",
            "Wednesday": "Legs",
            "Thursday": "Push Day (Chest & Triceps)",
            "Friday": "Shoulders",
            "Saturday": "Rest or Cardio",
            "Sunday": "Rest or Light Stretching"
        }


        # Initialize Tk root and hide it
        self.root = tk.Tk()
        self.root.withdraw()

        # Schedule the tasks
        schedule.every().day.at("22:02").do(self.morning_reminder)
        schedule.every().day.at("20:30").do(self.end_of_day_checkin)

        # Run the scheduler
        self.run_scheduler()

    # Get today's workout
    def get_todays_WO_plan(self):
        today = datetime.datetime.now().strftime("%A")
        return self.workout_schedule.get(today, "Rest or Custom Workout")

    # Function to show popup reminder
    def show_popup(self, title, message):
        def close_popup():
            popup.destroy()

        popup = tk.Toplevel()
        popup.title(title)

        # Add a label with the message
        label = tk.Label(popup, text=message, padx=20, pady=20)
        label.pack()

        # Add an OK button
        ok_button = tk.Button(popup, text="OK", command=close_popup, padx=10, pady=5)
        ok_button.pack()


        popup.mainloop()

    # Morning reminder function
    def morning_reminder(self):
        workout = self.get_todays_WO_plan()
        workout_message = f"Good morning! Today is {datetime.datetime.now().strftime('%A')}, and your workout is: {workout}"
        self.show_popup("Workout Reminder",
                        workout_message)

    # End of day check-in function
    def end_of_day_checkin(self):
        def check_response(response):
            if response == 'yes':
                self.show_popup("Great Job!", "Great job! Keep it up!")
            else:
                self.show_popup("No Worries!", "Don't worry, you'll get it next time!")
            popup.destroy()

        popup = tk.Toplevel()
        popup.title("Workout Check-In")

        # Add a label with the question
        label = tk.Label(popup, text="Did you complete your workout today?", padx=20, pady=20)
        label.pack()

        # Add Yes and No buttons
        yes_button = tk.Button(popup, text="Yes", command=lambda: check_response('yes'), padx=10, pady=5)
        yes_button.pack(side=tk.LEFT, padx=10)

        no_button = tk.Button(popup, text="No", command=lambda: check_response('no'), padx=10, pady=5)
        no_button.pack(side=tk.LEFT, padx=10)

        popup.mainloop()

    # Run the scheduler
    def run_scheduler(self):
        while True:
            schedule.run_pending()
            time.sleep(1)


# Instantiate and run the application
if __name__ == "__main__":
    app = Application()
