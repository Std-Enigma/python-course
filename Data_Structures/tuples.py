# Session 12 - Tuples

# 1. Creating a tuple
person = ("John", 25, "Engineer")
print("Tuple:", person)

# 2. Accessing elements in a tuple
print("Name:", person[0])
print("Age:", person[1])

# 3. Tuple packing and unpacking
name, age, profession = person
print(f"Name: {name}, Age: {age}, Profession: {profession}")
