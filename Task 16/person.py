# Grand Parent --parent  - child

class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return f"Name : {self.__name}"

    def get_age(self):
        return f"Age : {self.__age}"

    def set_age(self, age):
        if 20 < age < 60:
            self.__age = age
            print("Age Updated")
        else:
            print("Invalid Age")

    def person_info(self):
        return f"Name : {self.__name}\nAge : {self.__age}"


# Parent Class

class Employee(Person):

    def __init__(self, name, age, salary, company):
        super().__init__(name, age)
        self.__salary = salary
        self.__company = company

    def get_salary(self):
        return f"Salary : {self.__salary}"

    def get_company(self):
        return f"Company : {self.__company}"

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
            print("Salary Updated")
        else:
            print("Invalid Salary")

    def employee_info(self):
        print(self.person_info())
        print(f"Salary : {self.__salary}")
        print(f"Company : {self.__company}")


# Child of Employee

class Manager(Employee):

    def __init__(self, name, age, salary, company, team_size, bonus):
        super().__init__(name, age, salary, company)
        self.__team_size = team_size
        self.__bonus = bonus

    def get_team_size(self):
        return f"Team Size : {self.__team_size}"

    def get_bonus(self):
        return f"Bonus : {self.__bonus}"

    def set_team_size(self, team_size):
        if team_size > 0:
            self.__team_size = team_size
            print("Team Size Updated")
        else:
            print("Invalid Team Size")

    def set_bonus(self, bonus):
        if bonus <= (10/100) * self.__bonus:
            self.__bonus += bonus
            print(f"Bonus Updated : {self.__bonus}")
        else:
            print("Please update the bonus less than or equal to 10% of current bonus")

    def manager_info(self):
        self.employee_info()
        print(f"Team Size : {self.__team_size}")
        print(f"Bonus : {self.__bonus}")


manager = Manager("Greesha", 23, 75000, "TCS", 8, 15000)

print(manager.get_name())
print(manager.get_age())
print(manager.get_salary())
print(manager.get_company())
print(manager.get_team_size())
print(manager.get_bonus())

manager.manager_info()