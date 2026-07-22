class Person:
    def __init__(self, age):
        self.set_age(age)

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if 0 <= new_age <= 120:
            self.__age = new_age
            print("age of a student")
        else:
            print("Error: Age must be between 0 and 120.")
    def display_details(self):
        print(f"age:{self.__age}")      

perage = Person(20)
perage.display_details()
perage.set_age(150)
perage.display_details()        