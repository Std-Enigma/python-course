# Session 5 - Conditional Statements

# 1. Simple if statement
age = 17
if age >= 18:
    print("You are eligible to vote.")

# 2. if-else statement
num = 5
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")

# 3. if-elif-else statement
marks = 36
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: D")

# 4. Nested if statements
salary = 4000
if salary > 3000:
    if salary > 5000:
        print("High salary")
    else:
        print("Moderate salary")
else:
    print("Low salary")
