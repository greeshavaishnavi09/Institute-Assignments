#Take a number n from the user. Using while loop, print all prime numbers between 2 and n.

num = 2

prime_num =[]
while num <=10:
    if num % 2==0:
        prime_num.append("prime numbers")

    else:
        prime_num.append("Not a prime numbers")

    num+=1
print(prime_num)        
