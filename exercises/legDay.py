import random


class LegsWorkout:
    def __init__(self):

        self.legWarmUp = {
            "Jump Lunges": "",
            "Deadlifts": "",
            "Jump Rope": "",
            "Resistence Band Side to Side Lunges": ""
        }

        self.glutes = {
            "Resistence Band Glute Kick" : "",
            "Cable Pull Through" : "",
            "Deadlifts" : "",
            "Kettlebell Swing" : "",
            "Hip Thrust" : "",
            "Sumo Deadlift" : "",
            "Reverse Lunges" : "",
            "Leg curls" : "",
            "TOE UP HIP LIFT" : "",
            "STEP UP" : "",
            "TOE DOWN (STAB) HIP LIFT" : ""
        }

        self.quads = {
            "Leg Press" : "",
            "Leg Extension" : "",
            "Jump Lunges": "",
            "Dumbbell Lunge" : "",
            "Dumbbell Rear Lunge" : "",
            "Frog Squat" : "",
        }

        self.hams = {
            "Deadlifts" : "",
            "Romanian Deadlift": "",
            "Lying Leg Curls": "",
            "Seated Ham Curls": "",
            "Good Mornings": "",
            "Kettlebell swing": "",
            "Stiff-Legged Deadlift": "",
            "Sumo Deadlifts" : ""
        }

        self.calfs = {
            "Seated Calf Raise": "",
            "Standing Calf Raise": "",
            "1-½ CALF RAISES" : ""
        }

        # Initialize the workout plan
        self.legDayWOplan = {}

    def returnExercise(self, muscle_group):
        random_key = random.choice(list(muscle_group.keys()))
        random_value = muscle_group[random_key]
        return f"{random_key} - {random_value}"

    def legDay(self):
        legsWarmUp = self.returnExercise(self.legWarmUp)
        glutes = self.returnExercise(self.glutes)
        glutes2 = self.returnExercise(self.glutes)
        quads = self.returnExercise(self.quads)
        quads2 = self.returnExercise(self.quads)
        hams = self.returnExercise(self.hams)
        calfs = self.returnExercise(self.calfs)


        self.legDayWOplan["Legs Warm Up"] = legsWarmUp
        self.legDayWOplan["Glutes 1"] = glutes
        self.legDayWOplan["Glutes 2"] = glutes2
        self.legDayWOplan["Quads 1"] = quads
        self.legDayWOplan["Quads 2"] = quads2
        self.legDayWOplan["Hams"] = hams
        self.legDayWOplan["Calfs"] = calfs


        return self.legDayWOplan

    # Example usage
if __name__ == "__main__":
    workout = LegsWorkout()
    plan = workout.legDay()
    print(plan)
