#Question 9: 
#Python 
# Take a password from user. 
# Check if password is strong: 
# - Length >= 8 
# - Contains '@' or '#' 
# Print "Strong Password" or "Weak Password" 

password = input("Enter a password:")
password_len = len(password)

if password_len >= 8 and ("@" in password or "#" in password):    
    print("password is strong")
else:
    print("weak password")    
