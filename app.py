import datetime
import schedule
import time
import tkinter as tk
from tkinter import messagebox

# Define your workout schedule
workout_schedule = {
    "Monday": "Pull Day (Back & Biceps)",
    "Tuesday": "Biceps",
    "Wednesday": "Legs",
    "Thursday": "Push Day (Chest & Triceps)",
    "Friday": "Shoulders",
    "Saturday": "Rest or Cardio",
    "Sunday": "Rest or Light Stretching"
}


# Get today's workout
def get_todays_workout():
    today = datetime.datetime.now().strftime("%A")
    return workout_schedule.get(today, "Rest or Custom Workout")


# Function to show popup reminder
def show_popup(title, message):
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
def morning_reminder():
    workout = get_todays_workout()
    show_popup("Workout Reminder",
               f"Good morning! Today is {datetime.datetime.now().strftime('%A')}, and your workout is: {workout}")


# End of day check-in function
def end_of_day_checkin():
    def check_response(response):
        if response == 'yes':
            show_popup("Great Job!", "Great job! Keep it up!")
        else:
            show_popup("No Worries!", "Don't worry, you'll get it next time!")
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


# Schedule the tasks
schedule.every().day.at("09:00").do(morning_reminder)
schedule.every().day.at("20:30").do(end_of_day_checkin)

# Initialize Tk root and hide it
root = tk.Tk()
root.withdraw()

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
