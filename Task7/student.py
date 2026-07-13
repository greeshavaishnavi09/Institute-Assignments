
marks = (74,49,72,84,45)

average = sum(marks)/5

if average >=60 :
    if all(m > 40 for m in marks):
        print("Pass with Good Performance") 
    else:
        print("Pass but Weak in some subjects")
else:
    print("Fail")            