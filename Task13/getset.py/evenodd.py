#Python 
# Take a number from user. 
# Check whether the number is: 
# Positive AND Even 
# OR 
# Negative OR Odd 
# Print appropriate message

num = int(input("Enter a number:"))
if num > 0 and num % 2 == 0:
    print("Positive and Even number")
      
elif num < 0 or num % 2 != 0:
    print("Negative Or Odd number")
    
else:
    print("None")        
        
        
