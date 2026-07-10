#Take a year as input. Check if it is a leap year or not. (A year is leap if divisible by 4, but not by 100, unless also divisible by 400)

year= int(input("Enter a year"))
month_days=[0,31,28,31,30,31,30,31,31,30,31,30,31]
for n in year % 4 == 0 and (year% 100 ==0 oryear% 400 ==0 ):