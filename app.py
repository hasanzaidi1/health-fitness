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
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    messagebox.showinfo(title, message)
    root.destroy()

# Morning reminder function
def morning_reminder():
    workout = get_todays_workout()
    show_popup("Workout Reminder", f"Good morning! Today is {datetime.datetime.now().strftime('%A')}, and your workout is: {workout}")

# End of day check-in function
def end_of_day_checkin():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    response = messagebox.askquestion("Workout Check-In", "Did you complete your workout today?")
    if response == 'yes':
        show_popup("Great Job!", "Great job! Keep it up!")
    else:
        show_popup("No Worries!", "Don't worry, you'll get it next time!")
    root.destroy()

# Schedule the tasks
schedule.every().day.at("12:28").do(morning_reminder)
schedule.every().day.at("20:00").do(end_of_day_checkin)

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
