# Take a mobile number as input (10 digits). 
# Print: 
# First 3 digits (network code) 
# Last 4 digits  
# Middle 3 digits 

num = (input("Enter phonenumber:"))

print(num[0:3])
print(num[-4:])
print(num[3:6])