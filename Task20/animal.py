class Animal:

    def __init__(self, name):
        self.Name = name

    def sound(self):
        print(f"{self.Name} sound :")


class Dog(Animal):

    def sound(self):
        print(f"{self.Name} Sound : Woof Woof")


class Cat(Animal):

    def sound(self):
        print(f"{self.Name} Sound : Meow Meow")


# Obj
dog = Dog("Leo")
cat = Cat("hello Kitty")

Animals = [dog, cat]

for animal in Animals:
    animal.sound()