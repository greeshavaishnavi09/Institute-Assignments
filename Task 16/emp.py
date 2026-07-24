class Employee:

    # Constructor

    def __init__(self, emp_id, salary):
        self.__emp_id = emp_id
        self.__salary = salary

    # Getter

    def get_emp_id(self):
        return f"Employee ID : {self.__emp_id}"

    def get_salary(self):
        return f"Salary : {self.__salary}"

    # Setter

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
            print("Salary Updated")
        else:
            print("Invalid Salary")

    # Parent Method

    def employee_info(self):
        return f"Employee ID : {self.__emp_id}\nSalary : {self.__salary}"


# Child Class

class Manager(Employee):

    # Constructor

    def __init__(self, emp_id, salary, department):
        super().__init__(emp_id, salary)
        self.__department = department

    # Getter

    def get_department(self):
        return f"Department : {self.__department}"

    # Setter

    def set_department(self, department):
        self.__department = department
        print("Department Updated")

    # Child Method

    def manager_info(self):
        print(self.employee_info())
        print(f"Department : {self.__department}")


manager = Manager(101, 80000, "AI & ML")

print(manager.get_emp_id())
print(manager.get_salary())
print(manager.get_department())

manager.manager_info()