# Sort the following list according to age.

students = [("Ram",22),("Amit",19),("Neha",25),("Raj",20)]

students.sort(key=lambda x: x[1]) # x[1] indicates index value like 0 and 1

print(students)