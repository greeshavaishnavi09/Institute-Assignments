class Employee:

    # Constructor
    def __init__(self, name):
        self.__name = name

    # Getter
    def get_name(self):
        return f"Employee Name : {self.__name}"

    # Setter
    def set_name(self, name):
        self.__name = name
        print("Name Updated")

    # Method
    def employee_info(self):
        return f"Employee Name : {self.__name}"


# Parent Class

class ITEmployee(Employee):

    # Constructor
    def __init__(self, name, department):
        super().__init__(name)
        self.__department = department

    # Getter
    def get_department(self):
        return f"Department : {self.__department}"

    # Setter
    def set_department(self, department):
        self.__department = department
        print("Department Updated")

    # Method
    def it_employee_info(self):
        print(self.employee_info())
        print(f"Department : {self.__department}")


# Child Class

class SoftwareEngineer(ITEmployee):

    # Constructor
    def __init__(self, name, department, programming_skills):
        super().__init__(name, department)
        self.__programming_skills = programming_skills

    # Getter
    def get_programming_skills(self):
        return f"Programming Skills : {self.__programming_skills}"

    # Setter
    def set_programming_skills(self, skills):
        self.__programming_skills = skills
        print("Programming Skills Updated")

    # Method
    def software_engineer_info(self):
        self.it_employee_info()
        print(f"Programming Skills : {self.__programming_skills}")


engineer = SoftwareEngineer("Greesha", "AI & ML", "Python")

print(engineer.get_name())
print(engineer.get_department())
print(engineer.get_programming_skills())

engineer.software_engineer_info()