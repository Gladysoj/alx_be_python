task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        reminder = f"High priority task: {task}. Please handle it as soon as possible."
    case "medium":
        reminder =f"Medium priority task:{task}. Try to get it done today."
    case "low":
        reminder = f"Low priority task:{task}. You can do it when you have free time."
    case _:
        reminder = f"Task: {task}. (Unkown priority level entered.)"

if time_bound == "yes":
    reminder += "This task requires immediate attention today!"

    print(reminder)