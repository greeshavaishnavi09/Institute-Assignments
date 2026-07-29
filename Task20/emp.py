class Employee:

    def __init__(self, name, salary):
        self.Name = name
        self.Salary = salary

    def calculate_salary(self):
        print(f"{self.Name} Salary : {self.Salary}")


class Manager(Employee):

    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.Bonus = bonus

    def calculate_salary(self):

        total_salary = self.Salary + self.Bonus

        print(f"{self.Name} Total Salary : {total_salary}")


manager = Manager("Ramesh", 60000, 10000)

manager.calculate_salary()