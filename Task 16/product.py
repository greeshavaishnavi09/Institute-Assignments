class Product:

    # Constructor
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    # Getter
    def get_name(self):
        return f"Product Name : {self.__name}"

    # Getter
    def get_price(self):
        return f"Price : {self.__price}"

    # Setter
    def set_price(self, price):
        if price > 0:
            self.__price = price
            print("Price Updated")
        else:
            print("Invalid Price")

    # Method
    def product_info(self):
        return f"Product : {self.__name}\nPrice : {self.__price}"


# Parent Class

class Electronics(Product):

    # Constructor
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.__warranty = warranty

    # Getter
    def get_warranty(self):
        return f"Warranty : {self.__warranty} Years"

    # Setter
    def set_warranty(self, warranty):
        self.__warranty = warranty
        print("Warranty Updated")

    # Method
    def electronics_info(self):
        print(self.product_info())
        print(f"Warranty : {self.__warranty} Years")


# Child Class

class Smartphone(Electronics):

    # Constructor
    def __init__(self, name, price, warranty, ram, storage):
        super().__init__(name, price, warranty)
        self.__ram = ram
        self.__storage = storage

    # Getter
    def get_ram(self):
        return f"RAM : {self.__ram} GB"

    def get_storage(self):
        return f"Storage : {self.__storage} GB"

    # Setter
    def set_ram(self, ram):
        self.__ram = ram
        print("RAM Updated")

    def set_storage(self, storage):
        self.__storage = storage
        print("Storage Updated")

    # Method
    def smartphone_info(self):
        self.electronics_info()
        print(f"RAM : {self.__ram} GB")
        print(f"Storage : {self.__storage} GB")


mobile = Smartphone("Samsung S24", 85000, 2, 12, 256)

print(mobile.get_name())
print(mobile.get_price())
print(mobile.get_warranty())
print(mobile.get_ram())
print(mobile.get_storage())

mobile.smartphone_info()