# Session 24 - Inheritance


class Animal:
    def __init__(self, species):
        self.species = species

    def speak(self):
        return f"The {self.species} makes a sound."


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__("Cat")
        self.name = name
        self.age = age

    def speak(self):
        return f"{self.name} says Meow!"


my_cat = Cat("Whiskers", 2)
print(my_cat.speak())
