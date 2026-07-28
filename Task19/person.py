class Person:
    def __init__(self,name,**kwargs):
        super().__init__(**kwargs)
        self.__name = name

    # Getter Methods
    def get_name(self):
        return self.__name

    # Setter
    def set_name(self, new_name):
        self.__name = new_name
        print("Updated Name:", self.__name)

    def show(self):
        print("Person Details")
        print("Name :", self.__name)
       
class Employee(Person):
    def __init__(self,salary,**kwargs):
        super().__init__(**kwargs)
        self.__salary= salary
       
        #getter
    def get_salary(self):
            return self.__salary    


    #setter
    def set_salary(self,new_salary):
        if new_salary>0:
            self.__salary = new_salary
            print(f"updated salary:{self.__salary}")
        else:
             print("salary is invalid")

class Student(Person):
    def __init__(self,marks,**kwargs):
        super().__init__(**kwargs)
        self.__marks= marks

     #getter
    def get_marks(self):
            return self.__marks     
  

    #setter
    def set_marks(self,new_marks):
        if 0>=new_marks<=100:
            self.__marks = new_marks
            print(f"marks updated:{self.__marks}")
        else:
             print("marks must be below 0")


class TeachingAssistant(Employee, Student):
    def __init__(self,name,salary,marks, department,**kwargs):
        super().__init__(name=name,
                        salary=salary,
                        marks = marks,
                        **kwargs
                        )
        self.department = department

    def get_department(self):
        return self.department 


    def show(self):
        print("Person Details")
        print("Name :", self.get_name())
        print("salary :", self.get_salary())
        print("marks:", self.get_marks())
        print("department:", self.get_department())

ta = TeachingAssistant(name="Vaishnavi", salary=123456,marks= 80, department="Datascience"
                )  
ta.show() 