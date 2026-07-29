class Student:
    def details(self, name, age=None, city=None):
        if age is None and city is None:
            return f"Name: {name}"
        elif city is None:
            return f"Name: {name}, Age: {age}"
        else:
            return f"Name: {name}, Age: {age}, City: {city}"

s = Student()

print(s.details("Vaishnavi"))
print(s.details("Vaishnavi", 21))
print(s.details("Vaishnavi", 21, "Hyd"))
