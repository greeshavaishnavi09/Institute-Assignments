class Product:
    def __init__(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        self.__price = new_price
        print("new price value")

    def get_discounted_price(self, new_discount_percent):
        return self.__price - (self.__price * (new_discount_percent / 100))
    
    def display_details(self):
        print(f"price:{self.__price}")

prod = Product(200)
prod.display_details()
prod.set_price(500)
discounted_price = prod.get_discounted_price(30)
print(f"Discounted price: {discounted_price}")