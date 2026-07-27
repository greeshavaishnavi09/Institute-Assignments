
class Employee:

    total_emp = 0

    def __init__(self, name, salary, dept, **kwargs):
        super().__init__(**kwargs)
        self.__name = name
        self.__salary = salary
        self.__dept = dept
        Employee.total_emp += 1

    # Getter Methods
    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    def get_dept(self):
        return self.__dept

    # Static Method
    @staticmethod
    def set_sal(sal):
        if sal > 0:
            return sal
        else:
            return 0

    # Setter Method
    def set_salary(self, sal):
        self.__salary = Employee.set_sal(sal)

    # Class Method
    @classmethod
    def get_total(cls):
        return cls.total_emp

    # Normal Method
    def work(self):
        print("Employee is working")

    # Bonus
    def calculate_bonus(self):
        return self.__salary * 5/100

    # Show
    def show(self):
        print("Employee Details")
        print("Name :", self.__name)
        print("Salary :", self.__salary)
        print("Department :", self.__dept)
        print("Bonus :", self.calculate_bonus())


class Developer(Employee):

    def __init__(self, name, salary, dept, language,**kwargs):
        super().__init__(name = name, salary=salary, dept=dept,**kwargs)
        self.language = language

    # Override
    def work(self):
        print("Writing Code")

    # Override Bonus
    def calculate_bonus(self):
        return self.get_salary() * 2/100

    # Override Show
    def show(self):
        super().show()
        print("Language :", self.language)



class Designer(Employee):

    def __init__(self, name, salary, dept, tool,**kwargs):
        super().__init__(name=name, salary=salary, dept=dept,**kwargs)
        self.tool = tool

    # Override
    def work(self):
        print("Creating UI")

    # Override Bonus
    def calculate_bonus(self):
        return self.get_salary() * 15/100

    # Override Show
    def show(self):
        super().show()
        print("Tool :", self.tool)


class Manager(Employee):

    def __init__(self, name, salary, dept, team_size,**kwargs):
        super().__init__(name=name, salary=salary, dept=dept,**kwargs)
        self.team_size = team_size

    # Override
    def work(self):
        print("Managing Team")

    # Override Bonus
    def calculate_bonus(self):
        return self.get_salary() * 20/100

    # Override Show
    def show(self):
        super().show()
        print("Team Size :", self.team_size)


d1 = Developer("Vaishnavi", 50000, "IT", "Python")
d2 = Designer("Greesha", 45000, "Design", "chatgpt")
d3 = Manager("Tejaswi", 70000, "HR", 12)

d1.work()
d1.show()

d2.work()
d2.show()

d3.work()
d3.show()

print("Total Employees :", Employee.get_total())