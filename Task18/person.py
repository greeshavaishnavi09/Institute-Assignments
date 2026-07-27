class Person:

    def __init__(self, name, age, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.age = age
       
    # Show Method
    def show(self):
        print("Name :", self.name)
        print("Age :", self.age)

class Student(Person):

    def __init__(self, name, age,**kwargs):
        super().__init__(name=name, age=age,**kwargs)

class Teacher(Person):
    def __init__(self,name,age,**kwargs) :
        super().__init__(name=name, age=age,**kwargs)      


s1 = Student("Vaishnavi", 20)
t1 = Teacher("Greesha", 35)

print("Student Details")
s1.show()

print("Teacher Details")
t1.show()
