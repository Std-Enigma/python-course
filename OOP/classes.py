# Session 23 - Classes and Objects


# 1. Defining a class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"


# 2. Creating an object
my_dog = Dog("Buddy", 3)
print("Dog's Name:", my_dog.name)
print("Dog's Age:", my_dog.age)
print(my_dog.bark())
