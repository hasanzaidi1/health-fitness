import random


class PullDay:
    def __init__(self):
        self.lats = {
            "Lat Pulldown": "3x12 (130-140-150)",
            "V bar Lat Pulldown": "3x8 (130-135-140)",
            "Seated Row Machine": "3x10 (100-105-110)",
            "Cable Rope Pulldown": "3x10 (47-50-52)",
            "Wide Hand Pullups Body weight": "9-8-8",
            "Underhand close grip Pulldown": "3x10 (130-135-140)"
        }

        self.traps = {
            "Dumbbell Shrugs": 0,
            "EZ bar Upright Row": 0,
            "Face Pulls (with rope)": 0,
            "Rear Delt Fly (with rope)": 0
        }

        self.rearDelts = {
            "Bent-Over Row": 0,
            "Face Pulls (with rope)": 0,
            "Seated Bent-over lateral raise": 0,
            "Rear Delt Fly (with rope)": 0
        }

        self.spinalErectors = {
            "Deadlift": 0,
            "Bent-Over Row": 0,
            "Back Extensions": 0,
            "Glute Bridge": 0,
            "Prone Superman": 0
        }

        # Initialize the workout plan
        self.pullDayWOplan = {}

    def returnExercise(self, muscle_group):
        random_key = random.choice(list(muscle_group.keys()))
        random_value = muscle_group[random_key]
        return f"{random_key} - {random_value}"

    def pullDay(self):
        latsWO = self.returnExercise(self.lats)
        spinalErectorsWO = self.returnExercise(self.spinalErectors)
        rearDeltWO = self.returnExercise(self.rearDelts)
        trapsWO = self.returnExercise(self.traps)

        self.pullDayWOplan["Lats"] = latsWO
        self.pullDayWOplan["Spinal Erectors"] = spinalErectorsWO
        self.pullDayWOplan["Rear Delts"] = rearDeltWO
        self.pullDayWOplan["Traps"] = trapsWO

    def printWorkoutPlan(self):
        self.pullDay()
        print(self.pullDayWOplan)


# Instantiate the class and generate the workout plan
workout = PullDay()
workout.printWorkoutPlan()
