class Person:
    def __init__(self, age):
        self.__age = 0
        self.set_age(age)

    def display_all_details(self):
        print(f"Person Age: {self.__age}")

    def set_age(self, age):
        if 0 <= age <= 120:
            print("Age is in valid range (0-120)")
            self.__age = age
        else:
            print("Age should be between 0 and 120.")

    def get_age(self):
        return self.__age

per = Person(25)
per.set_age(135) 
per.set_age(30)   
per.display_all_details()
