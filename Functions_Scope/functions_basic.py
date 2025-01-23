# Session 8 - Functions Basics


# 1. Defining and calling a function
def greet(name):
    print(f"Hello, {name}!")


greet("Devil")
greet("Python Learner")


# 2. Function with arguments and return values
def add_numbers(a, b):
    return a + b


result = add_numbers(10, 20)
print("Sum:", result)


# 3. Positional and keyword arguments
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")


introduce("Devil", 25)  # Positional arguments
introduce(age=25, name="Devil")  # Keyword arguments
