#Take a character. Check if it is uppercase, lowercase, digit, or special character.

char = input("Enter a name")

if char.islower():
    print("lowercase character ")
elif char.isupper():
    print("uppercase character")
elif char.isdigit():
    print("digit is found") 
else:
    print("special character")       
