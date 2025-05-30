# pattern_drawing.py

try:
    # Prompt user for the size of the pattern
    size = int(input("Enter the size of the pattern: "))

    if size <= 0:
        print("Please enter a positive integer.")
    else:
        row = 0
        # Outer loop controls the rows using while
        while row < size:
            # Inner loop prints asterisks in one row using for
            for col in range(size):
                print("*", end="")
            print()  # Move to the next line after each row
            row += 1

except ValueError:
    print("Invalid input. Please enter a positive integer.")
