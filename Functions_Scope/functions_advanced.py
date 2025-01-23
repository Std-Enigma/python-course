# Session 9 - Advanced Functions


# 1. Default parameters
def greet(name, message="Welcome!"):
    print(f"Hello, {name}! {message}")


greet("Devil")
greet("Python Learner", "Good to see you!")


# 2. Recursive function: Factorial calculation
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


print("Factorial of 5:", factorial(5))

# 3. Anonymous (lambda) function
square = lambda x: x**2
print("Square of 3:", square(3))

# 4. Using a lambda function in map()
numbers = [1, 2, 3, 4]
squared_numbers = list(map(lambda x: x**2, numbers))
print("Squared numbers:", squared_numbers)
