#1. Student Class
#Create a Student class with
# name age marks
# Create two student objects and print all details using a method.

class Student:
    def __init__(self,name,age,marks):
        self.name= name
        self.age = age
        self.marks=marks

    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Marks: {self.marks}")    
    
student1 = Student("Vaishu",25,90)
student2 = Student("Greesha",21,89)

student1.display_details()
student2.display_details()




