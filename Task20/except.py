try:
    # Take value from the user side
    user_input = input("Enter a number: ")
    a = int(user_input)

except Exception as e:
    # Error message if user types letters or symbols
    print(f"Error: {e}")

else:
    # This runs only if the try block succeeds without errors
    if a % 2 == 0:
        print(f"{a} is Even.")
    else:
        print(f"{a} is Odd.")

finally:
    # Always runs at the end
    print("Program Executed Successfully")
