class Student:
    def __init__(self,total_classes,attended_classes):
        self.total_classes = total_classes
        self.attended_classes = attended_classes
    def display_details(self):
        print(f" total_classes:{self.total_classes},attended_classes={self.attended_classes}")
    def mark_attendance(self,number):
        if self.attended_classes + number <= self.total_classes:
            self.attended_classes += number
            percentage = (self.attended_classes / self.total_classes) * 100
            print(f"[Success] Marked {number} new classes.")
            print(f"Updated Attended Classes: {self.attended_classes}")
            print(f"Attendance Percentage: {percentage:.2f}%")
        else:
            max_allowed = self.total_classes - self.attended_classes
            print(f"[Error] Cannot mark {number} classes. Only {max_allowed} classes remaining.")

stu = Student(65,48)
stu.display_details()
stu.mark_attendance(10)
stu.mark_attendance(20)
