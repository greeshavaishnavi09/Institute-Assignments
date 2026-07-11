#Take a number. Check if it is divisible by both 3 and 5. If yes print "FizzBuzz", by 3 print "Fizz", by 5 print "Buzz", else print the number.

num = int(input("Enter a num"))
if (num % 3==0 and num % 5==0):
    print("FizzBuzz")
elif num% 3==0:
    print("Fizz") 
elif num% 5==0:
    print("Buzz")       
else:
    print(num)    
