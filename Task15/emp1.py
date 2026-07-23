from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return f"Employee Name : {self.__name}"

    def set_name(self, name):
        self.__name = name
        return "Name Updated"

    @abstractmethod
    def calculate_bonus(self):
        pass

    def employee_info(self):
        return f"Employee : {self.__name}"


class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.__salary = salary

    def calculate_bonus(self):
        bonus = self.__salary * 20 / 100
        print(self.employee_info())
        print(f"Salary : {self.__salary}")
        print(f"Bonus : {bonus}")


manager = Manager("Sumit", 80000)

print(manager.get_name())
print(manager.employee_info())
manager.calculate_bonus()