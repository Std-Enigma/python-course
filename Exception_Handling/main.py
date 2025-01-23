# Session 21 - Exception Handling

# 1. Basic exception handling
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input! Please enter a valid number.")

# 2. Handling multiple exceptions
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print("An error occurred:", e)

# 3. Finally block
try:
    file = open("non_existent_file.txt", "r")
except FileNotFoundError:
    print("File not found!")
finally:
    print("Execution completed.")
