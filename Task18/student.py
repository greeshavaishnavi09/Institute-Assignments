class Person:

    def __init__(self, name, age,**kwargs):
        super().__init__(**kwargs)
        self.__name = name
        self.__age = age

    # Getter Methods
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    # Show Method
    def show(self):
        print("Name :", self.__name)
        print("Age :", self.__age)


class Student(Person):

    def __init__(self, name, age, marks,**kwargs):
        super().__init__(name=name, age=age,**kwargs)
        self.marks = marks

    # Show Method
    def show(self):
        super().show()
        print("Marks :", self.marks)


class Teacher(Person):

    def __init__(self, name, age, subject,**kwargs):
        super().__init__(name=name, age=age,**kwargs)
        self.subject = subject

    # Show Method
    def show(self):
        super().show()
        print("Subject :", self.subject)


s1 = Student("Vaishnavi", 20, 95)
t1 = Teacher("Greesha", 35, "Mathematics")

print("Student Details")
s1.show()

print("Teacher Details")
t1.show()