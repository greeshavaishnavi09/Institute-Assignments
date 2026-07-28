class Vehicle:
    def __init__(self, brand, **kwargs):
        super().__init__(**kwargs)
        self.__brand = brand

    # Getter
    def get_brand(self):
        return self.__brand

    # Setter
    def set_brand(self, new_brand):
        self.__brand = new_brand
        print("Updated Brand:", self.__brand)

    def start(self):
        print(f"{self.__brand} Vehicle Started")


class Car(Vehicle):
    def __init__(self, model, **kwargs):
        super().__init__(**kwargs)
        self.__model = model

    # Getter
    def get_model(self):
        return self.__model

    # Setter
    def set_model(self, new_model):
        self.__model = new_model
        print("Updated Model:", self.__model)

    def drive(self):
        print(f"{self.__model} Car is Driving")


class Electric:
    def __init__(self, battery_capacity, **kwargs):
        super().__init__(**kwargs)
        self.__battery_capacity = battery_capacity

    # Getter
    def get_battery_capacity(self):
        return self.__battery_capacity

    # Setter
    def set_battery_capacity(self, new_capacity):
        if new_capacity > 0:
            self.__battery_capacity = new_capacity
            print("Updated Battery Capacity:", self.__battery_capacity)
        else:
            print("Invalid Battery Capacity")

    def battery(self):
        print(f"Battery Capacity : {self.__battery_capacity} ")


class ElectricCar(Car, Electric):
    def __init__(self, brand, model, battery_capacity, price, **kwargs):
        super().__init__(
            brand=brand,
            model=model,
            battery_capacity=battery_capacity,
            **kwargs
        )
        self.__price = price

    # Getter
    def get_price(self):
        return self.__price

    # Setter
    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
            print("Updated Price:", self.__price)
        else:
            print("Invalid Price")

    def show(self):
        print("Electric Car Details")
        print("Brand :", self.get_brand())
        print("Model :", self.get_model())
        print("Battery :", self.get_battery_capacity())
        print("Price :", self.get_price())

        self.start()
        self.drive()
        self.battery()

ec = ElectricCar(
    brand="Tesla",
    model="Model 3",
    battery_capacity=75,
    price=5500000
)

ec.show()