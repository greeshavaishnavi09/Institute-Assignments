from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return f"Animal Name : {self.__name}"

    def set_name(self, name):
        self.__name = name
        return "Name Updated"

    @abstractmethod
    def make_sound(self):
        pass

    def animal_info(self):
        return f"Animal : {self.__name}"


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.__breed = breed

    def make_sound(self):
        print(self.animal_info())
        print(f"Breed : {self.__breed}")
        print("Dog Sound : Bow Bow")


dog = Dog("Tommy", "Labrador")

print(dog.get_name())
print(dog.animal_info())
dog.make_sound()