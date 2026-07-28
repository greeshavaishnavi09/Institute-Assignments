class Car:
    def start(self):
        print("Car started with engine")

class Bicycle:
    def start(self):
        print("Bicycle started with pedals")

 # make function

def start_vehicle(vehicle):
    vehicle.start()

def display(vehicle):
    vehicle.start()


# Create objects
c = Car()
b = Bicycle()

display(c)
display(b)
