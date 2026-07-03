#Question 3: 
#Python 
# Take a number from user. 
# Check if the number is between 50 and 100 (using 'and') 
# Also check if it is NOT divisible by 5 (using 'not')

num = int(input("Enter a number"))
if not num % 5==0  and num >=50 <=100:
    print("True")
else:
    print("False")
