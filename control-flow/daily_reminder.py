# daily_reminder.py

# Prompt user for inputs
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").lower().strip()
time_bound = input("Is it time-bound? (yes/no): ").lower().strip()

# Valid input sets for validation
valid_priorities = {"high", "medium", "low"}
valid_time_bound = {"yes", "no"}

# Validate inputs before processing
if not task:
    print("Task description cannot be empty.")
elif priority not in valid_priorities:
    print("Invalid priority level. Please enter high, medium, or low.")
elif time_bound not in valid_time_bound:
    print("Invalid input for time-bound. Please enter yes or no.")
else:
    # Inputs valid: provide customized reminder based on priority and time sensitivity
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
                print(f"\nReminder: '{task}' is a low priority task. Consider completing it when you have free time.")
