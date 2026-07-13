#Take three numbers. First check if all three are equal. If not, check which one is the largest. Also check if the largest number is even or odd and print all information accordingly.

a=12
b=6
c=15
if a==b==c:
    print("all three num are equal")
else:
    if a>b and a>c:
        largest = a
        name = "a"
    elif b>c and b>a:
        largest = b 
        name = "b"
    else:  
        largest = c
        name = "c"
    print(f"largest num is {name}")

if largest % 2==0 :
    print("even num")
else:
    print("odd num")
            

