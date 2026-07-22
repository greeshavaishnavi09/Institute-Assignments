class Mobile:
    def __init__(self, price):
        self.__price = 1  
        self.set_price(price)

    def display_all_details(self):
        print(f"Mobile Price: {self.__price}")

    # --- Setter and Getter for Price ---
    def set_price(self, price):
        if price > 0:
            print("Price is a positive number")
            self.__price = price
        else:
            print("Price must be a positive number.")

    def get_price(self):
        return self.__price


mob = Mobile(15000)
mob.set_price(-500)  # Invalid
mob.set_price(18000) # Valid
mob.display_all_details()
