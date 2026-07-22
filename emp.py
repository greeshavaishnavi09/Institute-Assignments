class Employee:
    def __init__(self, salary):
        self.set_salary(salary)

    def get_salary(self):
        return self.__salary

    def set_salary(self,new_salary):
        if new_salary >= 5000:
            self.__salary = new_salary
            print("salary increased")
        else:
            print("Error: Salary cannot be below 5000.")
    def display_details(self):
        print(f"salary:{self.__salary}")      

emp = Employee(20000)
emp.display_details()
emp.set_salary(600)
emp.display_details()
