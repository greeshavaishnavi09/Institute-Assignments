# food management
from abc import ABC , abstractmethod
class Food(ABC):
    # constructor :
    def __init__(self,f_name,f_price):
        self.__Food_name = f_name
        self.__Food_price = f_price

    # getter name 
    def get_food_name(self):
        return self.__Food_name

    # getter price
    def get_food_price(self):
      return self.__Food_price

    # abstract method 1:
    @abstractmethod
    def prepare(self):
      pass

   # abstract method 2:

    @abstractmethod 
    def deliver(self):
       pass
    
    # display all details 

    def display_all_details(self):

        print(f"Food Name  : {self.__Food_name}")

        print(f"Food Price  : {self.__Food_price}")

        self.prepare()

        self.deliver()
    
# child class

class Pizza(Food):

    def prepare(self):
        print('Pizza is prepared ')

    def deliver(self):
        print("Pizza is Delivered")

# child class 2:

class Burger(Food):

    def prepare(self):
       print('Burger is prepared ')

    def deliver(self):
       print("Burger is Delivered") 

# child class 3:

class Biryani(Food):    

    def prepare(self):
        print('Biryani is prepared ')

    def deliver(self):
      print("Biryani is Delivered") 

# create the class object
pizza = Pizza("Pizza",500)
burger = Burger("Burger",200)
birynai = Biryani("Biryani",700)

pizza.display_all_details()
birynai.display_all_details()
burger.display_all_details()