try:

    numbers = input("Enter Numbers: ").split()

    integer_list = []

    for i in numbers:
        integer_list.append(int(i))

    print(integer_list)

except ValueError:
    print("Invalid Number Found.")