class Vehicle:

    # Parent Method
    def start(self):
        print("Vehicle is starting")


class Car(Vehicle):

    def __init__(self):
        super().__init__()


class Bike(Vehicle):

    def __init__(self):
        super().__init__()


c1 = Car()
b1 = Bike()

print("Car")
c1.start()

print("Bike")
b1.start()