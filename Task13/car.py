class Car:
    def __init__(self, model, year):
        self.__model = model  
        self.__year = year    

    def get_details(self):
        return f"Car Model: {self.__model}, Year: {self.__year}"
    
    def setter_year(self, new_year):
        if new_year > 2001:  
            self.__year = new_year
        else:
            print("Invalid year for a car.")

my_car = Car("Tesla Model 3", 2023)
print(my_car.get_details())

my_car.setter_year(2025)
print(my_car.get_details())
