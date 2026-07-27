
class Animal:

    # Parent Method
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    # Overriding Parent Method
    def sound(self):
        print("Dog barks")


class Cat(Animal):

    # Overriding Parent Method
    def sound(self):
        print("Cat meows")


d1 = Dog()
c1 = Cat()

print("Dog")
d1.sound()

print("Cat")
c1.sound()