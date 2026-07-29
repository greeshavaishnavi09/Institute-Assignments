class Vehicle:

    def __init__(self, name):
        self.Name = name

    def start(self):
        print(f"{self.Name} Vehicle Started")


class Car(Vehicle):

    def start(self):
        print(f"{self.Name} : Car Started with Key")


class Bike(Vehicle):

    def start(self):
        print(f"{self.Name}: Bike Started with kick")


car = Car("BMW")
bike = Bike("Royal Enfield")

Vehicles = [car, bike]

for vehicle in Vehicles:
    vehicle.start()