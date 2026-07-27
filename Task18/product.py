class Product:

    def __init__(self, price,**kwargs):
        super().__init__(**kwargs)
        self.__price = price

    # Getter Method
    def get_price(self):
        return self.__price

    # Show Method
    def show(self):
        print("Price :", self.__price)


class Electronics(Product):

    def __init__(self, price,**kwargs):
        super().__init__(price=price,**kwargs)


class Clothing(Product):

    def __init__(self, price,**kwargs):
        super().__init__(price=price,**kwargs)


e1 = Electronics(50000)
c1 = Clothing(2000)

print("Electronics Details")
e1.show()

print("Clothing Details")
c1.show()