class Student:
    def __init__(self, student_id, name, age, course, total_fees, total_classes):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.total_fees = total_fees
        self.fees_paid = 0
        self.marks = 0
        self.attended_classes = 0
        self.total_classes = total_classes

    def update_marks(self, marks):
        # Updates marks within a valid 0-100 range
        if 0 <= marks <= 100:
            self.marks = marks
            print(f"[Success] Marks updated to {self.marks} for {self.name}.")
        else:
            print(f"[Error] Invalid marks: {marks}")

    def pay_fees(self, amount):
        # Processes fee payments ensuring the user doesn't overpay.
        remaining_fee = self.total_fees - self.fees_paid
        if amount <= 0:
            print("[Error] Payment amount must be greater than zero.")
        elif amount > remaining_fee:
            print(f"[Error] Cannot pay {amount}. Remaining fee is only {remaining_fee}.")
        else:
            self.fees_paid += amount
            print(f"[Success] Paid {amount}. Remaining fee balance: {self.total_fees - self.fees_paid}.")

    def update_attendance(self, classes_attended):
        # Updates attended classes ensuring it does not exceed total classes scheduled.
        if classes_attended < 0:
            print("[Error] Attended classes cannot be negative.")
        elif classes_attended > self.total_classes:
            print(f"[Error] Cannot exceed scheduled total classes ({self.total_classes}).")
        else:
            self.attended_classes = classes_attended
            print(f"[Success] Attendance updated to {self.attended_classes}/{self.total_classes} classes.")

    def change_course(self, new_course, new_total_fees):
        # Changes the student's course and resets the base tuition cost.
        print(f"[Notice] Changing course from {self.course} to {new_course}.")
        self.course = new_course
        self.total_fees = new_total_fees
        # Fees paid carry over toward the new course pricing structure
        print(f"[Success] Course updated. New tuition balance: {self.total_fees - self.fees_paid}.")

    def calculate_attendance_percentage(self):
        # Computes the current raw attendance percentage.
        if self.total_classes == 0:
            return 0.0
        return (self.attended_classes / self.total_classes) * 100

    def check_pass_fail(self):
        # Checks if the student's marks meet the passing threshold (>= 35).
        return "Pass" if self.marks >= 35 else "Fail"

    def is_eligible_for_scholarship(self):
        # Checks strict criteria required to secure an academic scholarship.
        attendance_pct = self.calculate_attendance_percentage()
        is_fee_cleared = self.fees_paid >= self.total_fees
        
        if self.marks > 90 and attendance_pct > 95 and is_fee_cleared:
            return "Yes"
        return "No"

    def display_student_report(self):
        # Prints a completely structured report card outlining all criteria.
        attendance_pct = self.calculate_attendance_percentage()
        scholarship_status = self.is_eligible_for_scholarship()
        status = self.check_pass_fail()
        remaining_fee = self.total_fees - self.fees_paid

        print("\n" + "="*45)
        print(f"       UNIVERSITY STUDENT REPORT CARD        ")
        print("="*45)
        print(f"Student ID       : {self.student_id}")
        print(f"Name             : {self.name} (Age: {self.age})")
        print(f"Enrolled Course  : {self.course}")
        print("-"*45)
        print(f"Marks Secured    : {self.marks}/100 ({status})")
        print(f"Attendance       : {attendance_pct:.2f}% ({self.attended_classes}/{self.total_classes} Classes)")
        print(f"Fee Status       : Paid: {self.fees_paid} | Remaining: {remaining_fee}")
        print(f"Scholarship App  : {scholarship_status}")
        print("="*45 + "\n")


# Demonstration Flow 
# Creating student profile: ID 202601, Name 'Rahul', Age 20, Course 'B.Tech', Total Tuition 120000, Total Classes 100
student1 = Student(202601, "Rahul", 20, "B.Tech", 120000, 100)

student1.update_marks(95)
student1.pay_fees(120000)
student1.update_attendance(98)

# Output Final Structured Report
student1.display_student_report()
