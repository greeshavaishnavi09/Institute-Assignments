# Take a string from user. 
# Check if: 
# - The string length is greater than 5 
# - AND it starts with 'A' or 'a' 
# Print "Valid String" or "Invalid String" 

name = 'Greeshavaishavi'
len_name = len(name)
first_name1 = "A"
first_name2 = "a" 

if len_name > 5 and (first_name1 == 'A' or first_name2 == 'a') :
    print("Valid string")
else:
    print("Not a valid string")    