#Take a student's marks in 5 subjects. Calculate percentage and print grade according to these rules:
# 90 or above → A+
# 80–89 → A
# 70–79 → B
# 60–69 → C
# Below 60 → Fail Also print "Passed with Distinction" if percentage >= 75.

marks = (45,76,90,62,81)

per = sum(marks) / 5
print(per)
if per >= 90:
    print("grade A+")
elif 80>=per<=89:
    print("grade A") 
elif 70>=per<=79:
    print("grade B")
elif 60>=per<=69:  
    print("grade C")
else:
    print("Fail")    






