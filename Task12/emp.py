class Employee:
    def __init__(self,id,salary,pfmoney):
        self.__id = id
        self.__salary = salary
        self.__pfmoney = pfmoney
    def display_employee(self):
        print(f"id: {self.__id}, salary: {self.__salary}, pfmoney: {self.__pfmoney}")
    def get_salary(self):
        return self.__salary
    def get_salary(self):
        return self.__pfmoney
    def set_salary(self,new_salary):
        if self.__salary > 10000:
            self.__salary = new_salary
            print("salary increased")
        else:
            print("salary is not increased")    
    def set_pfmoney(self,new_pfmoney):
        if self.__pfmoney> 500:
            self.__pfmoney = new_pfmoney
            print("pf money increased")
        else:
            print("pf not increased")


emp = Employee(123,40000,5000)
emp.display_employee()
emp.set_salary(20000)
emp.set_pfmoney(200)
emp.display_employee()


   