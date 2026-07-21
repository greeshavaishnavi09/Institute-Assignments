class Student:
    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        self.__marks = marks

stu = Student(89)
print(stu.get_marks())

stu.set_marks(79)
print(stu.get_marks())