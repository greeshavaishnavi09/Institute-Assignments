try:

    # Write
    with open("student.txt", "w") as file:
        file.write("Name,Roll_No,Marks\n")
        file.write("Vaishnavi,1,85\n")
        file.write("teju,2,90\n")
        file.write("greesha,3,78\n")

    # Append
    with open("student.txt", "a") as file:
        file.write("sony,4,76\n")

    print("File created successfully.\n")

    # Read
    with open("student.txt", "r") as file:

        next(file)  # Skip header

        print("Name\t\tRoll_No\t\tMarks")
        print("-"*39)

        for line in file:
            Name, Roll_No, Marks = line.strip().split(",")
            print(f"{Name}\t\t{Roll_No}\t\t{Marks}")

except FileNotFoundError:
    print("File not found.")
    