try:

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    marks = float(input("Enter Marks: "))

    print("Name:", name)
    print("Age:", age)
    print("Marks:", marks)

except ValueError:
    print("Invalid Input.")

except TypeError:
    print("Invalid Type")    

except Exception as e:
    print("Something went wrong:", e)    

finally:
    print("Program Ended")