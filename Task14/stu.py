class Student:
    def __init__(self, marks):
        self.__marks = 0
        self.set_marks(marks)

    def display_all_details(self):
        print(f"Student Marks: {self.__marks}")

    # --- Setter and Getter for Marks ---
    def set_marks(self, marks):
        if 0 <= marks <= 100:
            print("Marks are in valid range (0-100)")
            self.__marks = marks
        else:
            print("Invalid marks! Must be between 0 and 100.")

    def get_marks(self):
        return self.__marks


std = Student(85)
std.set_marks(105)  
std.set_marks(92)   
std.display_all_details()
