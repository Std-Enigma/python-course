# Assignment 1: Personalized Greeting Program
# Objective: Create a program that greets the user based on their input and responds differently based on the time of day.

# Instructions:
# 1. Ask the user for their name and store it in a variable.
# 2. Ask the user what time of day it is (morning, afternoon, or evening).
# 3. Use if-elif-else statements to print a personalized greeting based on their name and the time of day.
#    - If it’s "morning," print: "Good morning, [name]! Have a great start to your day!"
#    - If it’s "afternoon," print: "Good afternoon, [name]! Hope your day is going well!"
#    - If it’s "evening," print: "Good evening, [name]! Enjoy the rest of your day!"
# 4. Include a message for any other input, like "I'm not sure what time that is, but hello, [name]!"
name = input("Please enter your name: ")
time_of_day = input("What time of day is it (morning, afternoon, evening)? ").lower()

if time_of_day == "morning":
    print(f"Good morning, {name}! Have a great start to your day!")
elif time_of_day == "afternoon":
    print(f"Good afternoon, {name}! Hope your day is going well!")
elif time_of_day == "evening":
    print(f"Good evening, {name}! Enjoy the rest of your day!")
else:
    print(f"I'm not sure what time that is, but hello, {name}!")

# Assignment 2: Simple Calculator
# Objective: Create a basic calculator that performs addition, subtraction, multiplication, and division.

# Instructions:
# 1. Ask the user to enter two numbers.
# 2. Ask the user which operation they would like to perform (addition, subtraction, multiplication, or division).
# 3. Use if-elif-else statements to perform the operation based on the user's input.
# 4. Display the result of the calculation to the user.
# Extra Challenge:
# - Add error handling for division by zero.
# - Ask if the user wants to perform another calculation and repeat if they answer "yes."
while True:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose an operation (+, -, *, /): ")

    if operation == "+":
        result = num1 + num2
        print("Result:", result)
    elif operation == "-":
        result = num1 - num2
        print("Result:", result)
    elif operation == "*":
        result = num1 * num2
        print("Result:", result)
    elif operation == "/":
        result = num1 / num2
        print("Result:", result)
    else:
        print("Invalid operation.")
        break

# Assignment 3: Guess the Number
# Objective: Create a number-guessing game where the program gives feedback on whether the guess is too high, too low, or correct.

# Instructions:
# 1. Choose a "secret" number (e.g., 7) and store it in a variable.
# 2. Ask the user to guess the number and store their guess.
# 3. Use comparison operators (<, >, ==) to check if their guess is:
#    - Equal to the secret number: Print "Congratulations! You guessed it!"
#    - Higher than the secret number: Print "Too high! Try again."
#    - Lower than the secret number: Print "Too low! Try again."
# 4. (Optional) Add a loop so they can keep guessing until they get the correct answer.
secret_number = 7
while True:
    guess = int(input("Guess the number: "))
    if guess == secret_number:
        print("Congratulations! You guessed it!")
        break
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")

# Assignment 4: Age Group Checker
# Objective: Write a program that categorizes a person’s age group based on their age.

# Instructions:
# 1. Ask the user to enter their age.
# 2. Use comparison and logical operators (and, or) to check which age range they fall into.
# 3. Print the appropriate age group based on their age:
#    - 0-12: Print "You are a child."
#    - 13-19: Print "You are a teenager."
#    - 20-64: Print "You are an adult."
#    - 65 and older: Print "You are a senior."
age = int(input("Please enter your age: "))

if 0 <= age <= 12:
    print("You are a child.")
elif 13 <= age <= 19:
    print("You are a teenager.")
elif 20 <= age <= 64:
    print("You are an adult.")
elif age >= 65:
    print("You are a senior.")
else:
    print("Invalid age entered.")

# Assignment 5: Scholarship Eligibility
# Objective: Determine if a student qualifies for a scholarship based on their grades and extracurricular involvement.

# Instructions:
# 1. Ask the user for their GPA (e.g., 3.5), and whether they participate in extracurricular activities (Yes/No).
# 2. Use comparison and logical operators to check eligibility:
#    - If GPA is 3.5 or higher and they participate in extracurriculars, print "Congratulations! You qualify for the scholarship."
#    - Otherwise, print "Unfortunately, you do not qualify for the scholarship."
gpa = float(input("Enter your GPA: "))
extracurricular = input(
    "Do you participate in extracurricular activities? (Yes/No): "
).lower()

if gpa >= 3.5 and extracurricular == "yes":
    print("Congratulations! You qualify for the scholarship.")
else:
    print("Unfortunately, you do not qualify for the scholarship.")
