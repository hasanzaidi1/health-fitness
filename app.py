import datetime
import tkinter as tk
import pyperclip  # Import pyperclip for clipboard operations
from exercises.pullDay import PullDay  # Import the PullDay class from pullDay.py
from exercises.pushDay import PushDay


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
            "Sunday": "Abs and Swimming"
        }

        # Initialize Tk root
        self.root = tk.Tk()
        self.root.withdraw()

        # Determine if it's morning or after 11:30 PM
        self.check_time_and_trigger()

    # Get today's workout
    def get_todays_WO_plan(self):
        today = datetime.datetime.now().strftime("%A")
        return self.workout_schedule.get(today, "Rest or Custom Workout")

    # Function to show popup reminder
    def show_popup(self, title, message):
        def close_popup():
            popup.destroy()

        def copy_to_clipboard():
            pyperclip.copy(message)  # Copy the message to clipboard
            copy_button.config(text="Copied!")  # Change button text to indicate success

        popup = tk.Toplevel()
        popup.title(title)

        # Add a label with the message
        label = tk.Label(popup, text=message, padx=20, pady=20)
        label.pack()

        # Add a Copy button
        copy_button = tk.Button(popup, text="Copy", command=copy_to_clipboard, padx=10, pady=5)
        copy_button.pack(side=tk.LEFT, padx=10)

        # Add an OK button
        ok_button = tk.Button(popup, text="OK", command=close_popup, padx=10, pady=5)
        ok_button.pack(side=tk.RIGHT, padx=10)

        popup.mainloop()

    # Morning reminder function
    def morning_reminder(self):
        today = datetime.datetime.now().strftime("%A")
        workout = self.get_todays_WO_plan()

        # Check if today is Pull Day
        if workout == "Pull Day (Back)":
            workout_message = (f"Good morning! Today is {today}, and your workout is: \n\n"
                               f"{self.get_pull_day_plan()}")
        elif workout == "Push Day (Chest & Triceps)":
            workout_message = (f"Good morning! Today is {today}, and your workout is: \n\n"
                               f"{self.get_push_day_plan()}")
        else:
            workout_message = f"Good morning! Today is {today}, and your workout is: {workout}"

        self.show_popup("Workout Reminder", workout_message)

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

    # Get Pull Day workout plan
    def get_pull_day_plan(self):
        workout = PullDay()
        plan = workout.pullDay()
        plan_message = "\n".join([f"{key}: {value}" for key, value in plan.items()])
        return plan_message

    # Get Biceps Day workout plan
    def get_biceps_day_plan(self):
        pass

    def get_legs_day_plan(self):
        pass

    def get_push_day_plan(self):
        workout = PushDay()
        plan = workout.pushDay()
        plan_message = "\n".join([f"{key}: {value}" for key, value in plan.items()])
        return plan_message


    def get_shoulders_day_plan(self):
        pass

    def get_abs_swim_day_plan(self):
        pass

    # Check the time and trigger the appropriate reminder
    def check_time_and_trigger(self):
        current_time = datetime.datetime.now().time()

        # Check if it's after 11:30 PM
        if current_time >= datetime.time(20, 30):
            self.end_of_day_checkin()
        else:
            self.morning_reminder()


# Instantiate and run the application
if __name__ == "__main__":
    app = Application()
