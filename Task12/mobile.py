# Mobile
# Create a Mobile class. Attributes brand model price Create a method that applies a 10% discount and updates price.

class Mobile:

    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price
    def display_details(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Price: {self.price}")

    def discount_price(self):
        self.price = int(self.price * 0.90)
        print(f"discount and updated price for {self.price}")     

mob = Mobile("realme","2pro",40000)
mob.display_details()
mob.discount_price()
