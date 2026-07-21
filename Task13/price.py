class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price  

item = Product("Laptop", 120000)

print(item.name)  

try:
    print(item.__price)
except AttributeError as e:
    print(f"Error: {e}")
