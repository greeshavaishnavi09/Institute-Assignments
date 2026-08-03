try:

    with open("phonebook.txt", "w") as file:

        file.write("Name,Phone_Number\n")
        file.write("Vaishu,9876543210\n")
        file.write("Teju,9876543211\n")
        file.write("Greesha,9876543212\n")

    print("Phonebook Created Successfully.\n")

    with open("phonebook.txt", "a") as file:

        file.write("Sony,9876543213\n")

    print("New Contact Added.\n")


    with open("phonebook.txt", "r") as file:

        next(file)      # Skip Header

        print("Name\t\tPhone_Number")
        print("-"*39)

        for line in file:

            Name, Phone = line.strip().split(",")

            print(f"{Name}\t\t{Phone}")

except FileNotFoundError:
    print("File Not Found")