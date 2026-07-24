class LivingBeing:

    # Constructor

    def __init__(self, name):
        self.__name = name

    # Getter

    def get_name(self):
        return f"Living Being : {self.__name}"

    # Setter

    def set_name(self, name):
        self.__name = name
        print("Name Updated")

    # Method

    def livingbeing_info(self):
        return f"Living Being : {self.__name}"

    # Method to Override

    def action(self):
        print("Living Being is Alive")


# Parent Class

class Animal(LivingBeing):

    # Constructor

    def __init__(self, name, food):
        super().__init__(name)
        self.__food = food

    # Getter

    def get_food(self):
        return f"Food : {self.__food}"

    # Setter

    def set_food(self, food):
        self.__food = food
        print("Food Updated")

    # Method

    def animal_info(self):
        print(self.livingbeing_info())
        print(f"Food : {self.__food}")

    # Method Overriding

    def action(self):
        print("Animal is Walking")


# Child Class

class Bird(Animal):

    # Constructor

    def __init__(self, name, food, wings):
        super().__init__(name, food)
        self.__wings = wings

    # Getter

    def get_wings(self):
        return f"Wings : {self.__wings}"

    # Setter

    def set_wings(self, wings):
        self.__wings = wings
        print("Wings Updated")

    # Method

    def bird_info(self):
        self.animal_info()
        print(f"Wings : {self.__wings}")

    # Method Overriding (Polymorphism)

    def action(self):
        print("Bird is Flying")


bird = Bird("Parrot", "Seeds", 2)

print(bird.get_name())
print(bird.get_food())
print(bird.get_wings())

bird.bird_info()
# Polymorphism (Method Overriding)
bird.action()