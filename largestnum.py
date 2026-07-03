#Question 4: 
#Python 
# Take three numbers from user. 
# Print the largest number using 'and' and 'or' operators.

a = 54
b = 68
c = 9
if a>= b and a>= c or b>= a and b>= c :
    if a>=b and a>=c:  #nested if logic
        greatest= a
    else:
        greatest =b
else:
    greatest= c
print(greatest)                

    


