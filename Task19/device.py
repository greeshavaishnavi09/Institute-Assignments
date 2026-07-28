class Device:
    def __init__(self, brand, **kwargs):
        super().__init__(**kwargs)
        self.__brand = brand

    # Getter
    def get_brand(self):
        return self.__brand

    # Setter
    def set_brand(self, new_brand):
        self.__brand = new_brand
        print("Updated Brand:", self.__brand)

    def power_on(self):
        print(f"{self.__brand} Device Powered On")


class Phone(Device):
    def __init__(self, phone_number, **kwargs):
        super().__init__(**kwargs)
        self.__phone_number = phone_number

    # Getter
    def get_phone_number(self):
        return self.__phone_number

    # Setter
    def set_phone_number(self, new_number):
        self.__phone_number = new_number
        print("Updated Phone Number:", self.__phone_number)

    def call(self):
        print(f"Calling from {self.__phone_number}")


class Camera:
    def __init__(self, megapixels, **kwargs):
        super().__init__(**kwargs)
        self.__megapixels = megapixels

    # Getter
    def get_megapixels(self):
        return self.__megapixels

    # Setter
    def set_megapixels(self, new_mp):
        if new_mp > 0:
            self.__megapixels = new_mp
            print("Updated Camera:", self.__megapixels)
        else:
            print("Invalid Camera")

    def click(self):
        print(f"Photo Clicked using {self.__megapixels}")


class SmartPhone(Phone, Camera):
    def __init__(self, brand, phone_number, megapixels, storage, **kwargs):
        super().__init__(
            brand=brand,
            phone_number=phone_number,
            megapixels=megapixels,
            **kwargs
        )
        self.__storage = storage

    # Getter
    def get_storage(self):
        return self.__storage

    # Setter
    def set_storage(self, new_storage):
        if new_storage > 0:
            self.__storage = new_storage
            print("Updated Storage:", self.__storage)
        else:
            print("Invalid Storage")

    def show(self):
        print("SmartPhone Details")
        print("Brand :", self.get_brand())
        print("Phone Number :", self.get_phone_number())
        print("Camera :", self.get_megapixels())
        print("Storage :", self.get_storage())

        self.power_on()
        self.call()
        self.click()


mobile = SmartPhone(
    brand="Samsung",
    phone_number="9876543210",
    megapixels=108,
    storage=256
)

mobile.show()