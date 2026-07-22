from abc import ABC, abstractmethod

class Transport(ABC):
    def __init__(self, model, max_speed):
        self.__model = model
        self.__max_speed = max_speed

    def get_model(self):
        return self.__model
        
    def get_max_speed(self):
        return self.__max_speed
    
    @abstractmethod
    def move(self):
        pass    
   
    @abstractmethod
    def fuel_type(self):
        pass
        
    def display_all_details(self):
        print(f"model : {self.__model}")
        print(f"max_speed : {self.__max_speed}")
        self.move()
        self.fuel_type()

class Car(Transport): 
    def move(self):
        print("move : Drives on roads  ")
        
    def fuel_type(self):
        print("fuel_type : Petrol, Diesel, or Electric Battery")

class Train(Transport):
    def move(self):
        print("move : Runs on tracks  ")
            
    def fuel_type(self):
        print("fuel_type : Overhead Electricity lines or Diesel engines")

class Airplane(Transport):
    def move(self):
        print("move : Flies through the air ")
                
    def fuel_type(self):
        print("fuel_type : Fuel")
    

car = Car("Tesla", 280)
train = Train("Vande Bharat", 210)
plane = Airplane("Boeing 777", 320)

car.display_all_details()
train.display_all_details()
plane.display_all_details()
