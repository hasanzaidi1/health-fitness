import random

lats = {
    "Lat Pulldown": "3x12 (130-140-150)",
    "V bar Lat Pulldown": "3x8 (130-135-140)",
    "Seated Row Machine": "3x10 (100-105-110)",
    "Cable Rope Pulldown": "3x10 (47-50-52)",
    "Wide Hand Pullups Body weight": "9-8-8",
    "Underhand close grip Pulldown": "3x10 (130-135-140)"
}

traps = {
    "Dumbbell Shrugs" : 0,
    "EZ bar Upright Row" : 0,
    "Face Pulls (with rope)" : 0,
    "Rear Delt Fly (with rope)" : 0
}

rearDelts = {
    "Bent-Over Row" : 0 ,
    "Face Pulls (with rope)" : 0 ,
    "Seated Bent-over lateral raise" : 0,
    "Rear Delt Fly (with rope)": 0
}

spinalErectors = {
    "Deadlift" : 0 ,
    "Bent-Over Row" : 0 ,
    "Back Extensions" : 0 ,
    "Glute Bridge" : 0 ,
    "Prone Superman" : 0
}


def returnExcercise(muscle_group):
    random_key = random.choice(list(muscle_group.keys()))
    # Get the value for the random key
    random_value = muscle_group[random_key]
    return (f"{random_key} - {random_value}")

pullDayWOplan = {}

def pullDay():
    latsWO = returnExcercise(lats)
    spinalErectorsWO = returnExcercise(spinalErectors)
    rearDeltWO = returnExcercise(rearDelts)
    trapsWO = returnExcercise(traps)

    pullDayWOplan["lats"] = latsWO
    pullDayWOplan["Spinal Erectors"] = spinalErectorsWO
    pullDayWOplan["Rear Delts"] = rearDeltWO
    pullDayWOplan["Traps"] = trapsWO


# Generate the workout plan
pullDay()

# Print the generated workout plan

print(pullDayWOplan)
