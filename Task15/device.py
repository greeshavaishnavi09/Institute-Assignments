from abc import ABC, abstractmethod

class Device(ABC):
    def __init__(self, brand):
        self.__brand = brand

    def get_brand(self):
        return f"Brand : {self.__brand}"

    def set_brand(self, brand):
        self.__brand = brand
        return "Brand Updated"

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    def device_info(self):
        return f"Brand : {self.__brand}"


class Laptop(Device):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.__model = model

    def turn_on(self):
        print(f"{self.__model} Laptop is Turning ON")

    def turn_off(self):
        print(f"{self.__model} Laptop is Turning OFF")


lap = Laptop("Dell", "Inspiron")

print(lap.get_brand())
print(lap.device_info())
lap.turn_on()
lap.turn_off()