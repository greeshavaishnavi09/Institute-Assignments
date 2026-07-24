class Vehicle:

    # Constructor

    def __init__(self, vehicle_no):
        self.__vehicle_no = vehicle_no

    # Getter

    def get_vehicle_no(self):
        return f"Vehicle Number : {self.__vehicle_no}"

    # Setter

    def set_vehicle_no(self, vehicle_no):
        self.__vehicle_no = vehicle_no
        print("Vehicle Number Updated")

    # Parent Method

    def start(self):
        print("Vehicle is Starting...")

    def vehicle_info(self):
        return f"Vehicle Number : {self.__vehicle_no}"


# Child Class

class Car(Vehicle):

    # Constructor

    def __init__(self, vehicle_no, brand):
        super().__init__(vehicle_no)
        self.__brand = brand

    # Getter

    def get_brand(self):
        return f"Brand : {self.__brand}"

    # Setter

    def set_brand(self, brand):
        self.__brand = brand
        print("Brand Updated")

    # Method Overriding

    def start(self):
        print(f"{self.__brand} Car is Starting...")

    # Child Method

    def car_info(self):
        print(self.vehicle_info())
        print(f"Brand : {self.__brand}")


car = Car("TS09AB1234", "Hyundai")

print(car.get_vehicle_no())
print(car.get_brand())

car.car_info()
car.start()