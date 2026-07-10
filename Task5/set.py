#Take three numbers as input from the user. Print the largest number and also check
#  whether all three numbers are equal or not.
num = {45,16,45}
largest = max(num)
print(largest)

num = list(num)
if num[0]==num[1]==num[2]:
    print("equal")
else:
    print("not equal")    




