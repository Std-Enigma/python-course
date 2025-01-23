# Example 1: Odd or Even Checker
# Objective: Determine if a number is odd or even based on user input.

# Instructions:
# 1. Ask the user to enter a number.
# 2. Use the modulo operator to check if the number is divisible by 2.
# 3. Print "Even" if the number is divisible by 2, otherwise print "Odd."
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Example 2: Counting Down from a Number
# Objective: Create a countdown from a starting number to zero.

# Instructions:
# 1. Ask the user for a starting number.
# 2. Use a while loop to decrement the number until it reaches zero.
# 3. Print each number in the countdown.
start = int(input("Enter a starting number: "))
while start >= 0:
    print(start)
    start -= 1

# Example 3: Simple Password Validator
# Objective: Validate a password entered by the user.

# Instructions:
# 1. Define a fixed password in the code (e.g., "python123").
# 2. Ask the user to enter a password.
# 3. Compare the entered password with the fixed password.
# 4. Print "Access granted!" if the passwords match, otherwise print "Access denied!".
password = "python123"
user_input = input("Enter the password: ")

if user_input == password:
    print("Access granted!")
else:
    print("Access denied!")

# Example 4: Sum of Numbers
# Objective: Calculate the sum of numbers from 1 to 10.

# Instructions:
# 1. Initialize a variable to store the total sum.
# 2. Use a for loop to iterate through numbers from 1 to 10.
# 3. Add each number to the total sum.
# 4. Print the final total.
total = 0
for i in range(1, 11):  # Change range as needed
    total += i

print("The sum of numbers from 1 to 10 is:", total)

# Example 5: Multiplication Table
# Objective: Display a multiplication table for a user-provided number.

# Instructions:
# 1. Ask the user for a number.
# 2. Use a for loop to iterate from 1 to 10.
# 3. Multiply the user's number by the current iteration value and print the result.
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Example 6: Guess the Number
# Objective: Create a simple guessing game.

# Instructions:
# 1. Define a fixed secret number (e.g., 7).
# 2. Ask the user to guess the number.
# 3. Use comparison operators to check if their guess is:
#    - Equal to the secret number: Print "Congratulations! You guessed it!"
#    - Higher: Print "Too high! Try again."
#    - Lower: Print "Too low! Try again."
secret = 7  # Fixed number for now
guess = int(input("Guess a number between 1 and 10: "))

if guess == secret:
    print("You guessed it!")
elif guess < secret:
    print("Too low!")
else:
    print("Too high!")

# Example 7: Reverse a Word
# Objective: Reverse a word entered by the user.

# Instructions:
# 1. Ask the user to input a word.
# 2. Use string slicing to reverse the word.
# 3. Print the reversed word.
word = input("Enter a word: ")
reversed_word = word[::-1]
print("Reversed word:", reversed_word)

# Example 8: Factorial Calculator
# Objective: Calculate the factorial of a user-provided number.

# Instructions:
# 1. Ask the user to enter a number.
# 2. Initialize a variable for the factorial result.
# 3. Use a for loop to multiply numbers from 1 to the user's number.
# 4. Print the calculated factorial.
num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"Factorial of {num} is {factorial}")

# Example 9: Find the Largest Number
# Objective: Determine the largest number from a set of user inputs.

# Instructions:
# 1. Use a list comprehension to gather 5 numbers from the user.
# 2. Use the max() function to find the largest number.
# 3. Print the result.
numbers = [int(input("Enter a number: ")) for _ in range(5)]
largest = max(numbers)
print("The largest number is:", largest)

# Example 10: Simple Number Sequence
# Objective: Display a sequence of numbers based on user input.

# Instructions:
# 1. Ask the user how many numbers to display.
# 2. Use a for loop to print numbers from 1 to the specified count.
n = int(input("How many numbers to display? "))
for i in range(1, n + 1):
    print(i, end=" ")
