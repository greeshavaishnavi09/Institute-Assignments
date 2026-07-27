class Animal:

    # Parent Method
    def eat(self):
        print("Animal is eating")

class Dog(Animal):

    def __init__(self):
        super().__init__()


class Cat(Animal):

    def __init__(self):
        super().__init__()

d1 = Dog()
c1 = Cat()

print("Dog")
d1.eat()

print("Cat")
c1.eat()