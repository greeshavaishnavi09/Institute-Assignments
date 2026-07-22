from abc import ABC, abstractmethod

class Company(ABC):
    def __init__(self, name, role):
        self.__name = name
        self.__role = role

    def get_name(self):
        return self.__name
        
    def get_role(self):
        return self.__role
        
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def salary(self):
        pass
        
    def display_all_details(self):
        print(f"Name : {self.__name}")
        print(f"Role : {self.__role}")
        self.work()
        self.salary()

class Employee(Company): 
    def work(self):
        print("Work : daily tasks")
        
    def salary(self):
        print("Salary : 50,000")

class Manager(Company):
    def work(self):
        print("Work : Manages teams and projects")
        
    def salary(self):
        print("Salary : 1,00,000")

employee = Employee("Vaishnavi", "Data Scientist")
manager = Manager("Sumit", "Project Manager")
manager.display_all_details()
employee.display_all_details()