# Employee Salary
#Create an Employee class.
#Attributes  emp_id name salary
# Create a method that increases salary by ₹5000 and prints updated salary.

class Employee:
    def __init__(self,emp_id ,name ,salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display_details(self):
        print(f"Emp_id: {self.emp_id}, Name: {self.name}, Salary: {self.salary}")

    def increase_salary(self):
        self.salary += 5000
        print(f"Updated Salary for {self.name}: {self.salary}")  

emp1 = Employee(101, "Amitha", 43000)
emp1.display_details()
emp1.increase_salary()

        