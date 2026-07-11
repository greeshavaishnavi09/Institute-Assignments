#Take a year as input. Check if it is a leap year or not. (A year is leap if divisible by 4, but not by 100, unless also divisible by 400)

year= 2020

if (year % 4 == 0 and year% 100!=0) or (year% 400 ==0 ):
    print("Leap Year")
else:
    print("Not a Leap Year")
