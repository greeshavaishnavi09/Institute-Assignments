from abc import ABC, abstractmethod

class GameCharacter(ABC):
    def __init__(self, name, health_points):
        self.__name = name
        self.__health_points = health_points

    @abstractmethod
    def attack(self): 
        pass

    def display_all_details(self):
        print(f"Name : {self.__name}")
        print(f"Health Points  : {self.__health_points}")
        self.attack()

class Warrior(GameCharacter):
    def attack(self):
        print("Combat Action  : Swings a massive iron sword up close! (Melee Damage)")

class Archer(GameCharacter):
    def attack(self):
        print("Combat Action  : Shoots piercing arrows from a long distance! (Ranged Damage)")

class Mage(GameCharacter):
    def attack(self): 
        print("Combat Action  : Casts explosive elemental fireballs using mana! (Magic Damage)")


knight = Warrior("Arthur", 150)
elf = Archer("Legolas", 100)
wizard = Mage("Gandalf", 80)

knight.display_all_details()
elf.display_all_details()
wizard.display_all_details()

    