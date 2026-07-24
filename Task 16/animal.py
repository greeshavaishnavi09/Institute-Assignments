class Animal:

    # Constructor

    def __init__(self, food):
        self.__food = food

    # Getter

    def get_food(self):
        return f"Food : {self.__food}"

    # Setter

    def set_food(self, food):
        self.__food = food
        print("Food Updated")

    # Method

    def eat(self):
        print(f"Animal eats {self.__food}")

    # Parent Method

    def animal_info(self):
        return f"Food : {self.__food}"


# Child Class

class Dog(Animal):

    # Constructor

    def __init__(self, food, breed):
        super().__init__(food)
        self.__breed = breed

    # Getter

    def get_breed(self):
        return f"Breed : {self.__breed}"

    # Setter

    def set_breed(self, breed):
        self.__breed = breed
        print("Breed Updated")

    # Method

    def bark(self):
        print("Dog is Barking...Bow Bow")

    # Child Method

    def dog_info(self):
        print(self.animal_info())
        print(f"Breed : {self.__breed}")


dog = Dog("Meat", "Labrador")

print(dog.get_food())
print(dog.get_breed())

dog.eat()
dog.bark()
dog.dog_info()