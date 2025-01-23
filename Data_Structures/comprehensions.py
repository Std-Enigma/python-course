# Session 15 - List and Dictionary Comprehensions

# 1. List comprehension
numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers]
print("Squares:", squares)

# 2. Dictionary comprehension
students = {"Alice": 85, "Bob": 92, "Charlie": 78}
passed_students = {name: marks for name, marks in students.items() if marks > 80}
print("Passed students:", passed_students)
