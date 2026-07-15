#Take a number n from user and print sum of first n natural numbers using for loop.

num =int(input("enter a num:"))
sum=0

for i in range(1,num+1):
        sum+=i
        print(sum)    
