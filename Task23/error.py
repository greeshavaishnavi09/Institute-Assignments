try:

    # Create File
    with open("log.txt","w") as file:

        file.write("INFO Login Success\n")
        file.write("ERROR Invalid Password\n")
        file.write("INFO File Opened\n")
        file.write("ERROR Database Error\n")

    print("Log File Created.\n")

    # Append
    with open("log.txt","a") as file:

        file.write("ERROR Network Error\n")

    print("New Log Added.\n")

   
    count = 0

    with open("log.txt","r") as file:

        print("Log Messages")
        print()

        for line in file:

            print(line.strip())

            if "ERROR" in line:
                count += 1

    print()
    print("Total ERROR Messages =", count)

except FileNotFoundError:
    print("File Not Found")