# daily_reminder.py

# Prompt user for task details
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").lower().strip()
time_bound = input("Is it time-bound? (yes/no): ").lower().strip()

# Validate inputs
if not task:
    print("Error: Task description cannot be empty.")
elif priority not in {"high", "medium", "low"}:
    print("Error: Priority must be 'high', 'medium', or 'low'.")
elif time_bound not in {"yes", "no"}:
    print("Error: Time-bound must be 'yes' or 'no'.")
else:
    # Compose reminder based on priority and time-bound status
    match priority:
        case "high":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"Reminder: '{task}' is a high priority task. Please address it as soon as possible.")
        case "medium":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a medium priority task that is time-sensitive. Try to complete it today.")
            else:
                print(f"Reminder: '{task}' is a medium priority task. Plan to work on it soon.")
        case "low":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a low priority task that still requires timely action today.")
            else:
                print(f"Reminder: '{task}' is a low priority task. Consider doing it when you have free time.")
