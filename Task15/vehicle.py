from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand):
        self.__brand = brand

    def get_brand(self):
        return f"Brand : {self.__brand}"

    def vehicle_info(self):
        return f"Brand : {self.__brand}"

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.__model = model

    def start(self):
        print(f"{self.__model} Car Started")

    def car_info(self):
        print(self.vehicle_info())
        print(f"Model : {self.__model}")


class ElectricCar(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.__battery = battery

    def battery_info(self):
        print(f"Battery : {self.__battery} kWh")


ev = ElectricCar("Tesla", "Model 3", 75)

print(ev.get_brand())
ev.car_info()
ev.start()
ev.battery_info()