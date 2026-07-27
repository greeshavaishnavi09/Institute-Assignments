class Person:

    # Class Variable
    total_persons = 0

    def __init__(self, name, age,**kwargs):
        super().__init__(**kwargs)
        self.__name = name
        self.__age = Person.validate_age(age)
        Person.total_persons += 1

    # Getter Methods
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    # Static Method
    @staticmethod
    def validate_age(age):
        if age > 0:
            return age
        else:
            return 0

    # Setter Method
    def set_age(self, age):
        self.__age = Person.validate_age(age)

    # Class Method
    @classmethod
    def get_total_persons(cls):
        return cls.total_persons

    # Show Method
    def show(self):
        print("Name :", self.__name)
        print("Age :", self.__age)


class Student(Person):

    def __init__(self, name, age, marks,**kwargs):
        super().__init__(name=name, age=age,**kwargs)
        self.marks = marks

    def show(self):
        super().show()
        print("Marks :", self.marks)


class Teacher(Person):

    def __init__(self, name, age, subject,**kwargs):
        super().__init__(name=name, age=age,**kwargs)
        self.subject = subject

    def show(self):
        super().show()
        print("Subject :", self.subject)

class Staff(Person):

    def __init__(self, name, age, department,**kwargs):
        super().__init__(name=name, age=age,**kwargs)
        self.department = department

    def show(self):
        super().show()
        print("Department :", self.department)

s1 = Student("Rahul", 20, 95)
t1 = Teacher("Priyanka", 35, "Mathematics")
st1 = Staff("Amitha", 40, "Administration")

s1.show()
print()

t1.show()
print()

st1.show()

print("Total Persons :", Person.get_total_persons())