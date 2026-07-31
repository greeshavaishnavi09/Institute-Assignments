
try:
    a = 15
    if a % 2 == 0:
            print(f"{a} is Even.")
    else:
        print(f"{a} is Odd.")

except Exception as e:
    print(e)

else:
   print("odd")

finally:
    print("Program Executed Successfully")
