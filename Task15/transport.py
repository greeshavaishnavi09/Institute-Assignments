from abc import ABC, abstractmethod

class Transport(ABC):
    def __init__(self, speed):
        self.__speed = speed

    def get_speed(self):
        return f"Speed : {self.__speed} km/hr"

    def set_speed(self, speed):
        if speed > 0:
            self.__speed = speed
            return "Speed Updated"
        else:
            print("Invalid Speed")

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def fuel_type(self):
        pass

    def transport_info(self):
        return f"Speed : {self.__speed} km/hr"


class Car(Transport):
    def __init__(self, speed, company):
        super().__init__(speed)
        self.__company = company

    def move(self):
        print(f"{self.__company} Car is Moving")

    def fuel_type(self):
        print("Fuel Type : Petrol")


car = Car(120, "Hyundai")

print(car.get_speed())
print(car.transport_info())
car.move()
car.fuel_type()