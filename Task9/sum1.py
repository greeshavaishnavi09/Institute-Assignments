# Keep taking numbers from user until they enter 0, then print sum.

sum=0

while True:
    num = int(input("Enter a num:"))
    if num == 0:
        break
    sum += num
print(sum)

    
    

