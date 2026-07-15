# Count how many numbers between 1 to 50 are divisible by 3 using for loop.

num = 1
count = 1
for i in range(1,50):
    if i % 3 ==0:
        count+=1
        print(i)
