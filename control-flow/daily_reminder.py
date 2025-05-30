# daily_reminder.py

# Get user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Display customized reminder using match-case (Python 3.10+)
match priority:
    case "high":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"\nReminder: '{task}' is a high priority task. Make sure to address it as soon as possible.")
    case "medium":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a medium priority task that is time-sensitive. Try to finish it today.")
        else:
            print(f"\nReminder: '{task}' is a medium priority task. Plan to work on it soon.")
    case "low":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a low priority task, but it's time-bound. Don’t let it slip!")
        else:
            print(f"\nNote: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("\nInvalid priority level. Please enter high, medium, or low.")
