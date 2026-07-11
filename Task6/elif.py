#Take age and gender. If age >= 18 and gender is "Male" print "Eligible for Army", elif age >= 18 and gender "Female" print "Eligible for Other Services", else print "Not Eligible".

age = int(input("Enter a num:"))
gender = input("Enter gender:")

if (age >=18 and gender == "Male"):
    print("Eligible for Army")
elif (age >= 18 and gender == "Female") :
    print("Eligible for Other Services")  
else:
    print("Not Eligible")     


