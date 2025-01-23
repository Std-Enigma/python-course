# Session 25 - Polymorphism


class Bird:
    def fly(self):
        return "Bird is flying."


class Airplane:
    def fly(self):
        return "Airplane is flying."


def let_it_fly(entity):
    print(entity.fly())


sparrow = Bird()
boeing = Airplane()

let_it_fly(sparrow)
let_it_fly(boeing)
