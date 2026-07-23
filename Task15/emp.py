from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def get_name(self):
        return f"Employee Name : {self.__name}"

    def get_salary(self):
        return f"Salary : {self.__salary}"

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
            return "Salary Updated"
        else:
            print("Invalid Salary")

    @abstractmethod
    def calculate_bonus(self):
        pass

    def employee_info(self):
        return f"Name : {self.__name}\nSalary : {self.__salary}"


class Developer(Employee):
    def __init__(self, name, salary, project):
        super().__init__(name, salary)
        self.__project = project

    def calculate_bonus(self):
        bonus = self._Employee__salary * 10 / 100
        print(self.employee_info())
        print(f"Project : {self.__project}")
        print(f"Bonus : {bonus}")


dev = Developer("Greesha", 60000, "Housing Price Prediction")

print(dev.get_name())
print(dev.get_salary())
dev.calculate_bonus()