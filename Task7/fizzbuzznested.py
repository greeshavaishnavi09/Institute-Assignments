#Take a number as input. Check if the number is positive. If positive, check if it is divisible by both 3 and 5. If yes, print "FizzBuzz". If only divisible by 3 print "Fizz", only by 5 print "Buzz". If negative, print "Negative Number".

num = int(input("Enter a num"))

if num >= 0:
    if num % 3==0 and num%5==0:
        print("FizzBuzz")
    else:
        if num %3==0:
            print("Fizz")
        if num % 5==0:
            print("Buzz")
        else:
            print("Postive num")
else:
    print("Negative num")                