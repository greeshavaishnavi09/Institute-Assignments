class Laptop:
    def __init__(self,brand,ram,storage):
        self.brand = brand
        self.ram = ram
        self.storage = storage

    def display_details(self):  
        print(f"Brand: {self.brand}, Ram: {self.ram}, Storage: {self.storage}")

    def upgrade_ram(self):
        self.ram += 8
        print(f"upgraded ram size : {self.ram}")

lap = Laptop("Lenovo",5,"512GB SSD")
lap.display_details()
lap.upgrade_ram()