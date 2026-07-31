try:

    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))
    operator = input("Enter Operator (+,-,*,/): ")

    if operator == "+":
        print("Answer:", num1 + num2)

    elif operator == "-":
        print("Answer:", num1 - num2)

    elif operator == "*":
        print("Answer:", num1 * num2)

    elif operator == "/":
        print("Answer:", num1 / num2)

    else:
        print("Invalid Operator")

except ValueError:
    print("Please enter only numbers.")

except ZeroDivisionError:
    print("Cannot divide by zero.")