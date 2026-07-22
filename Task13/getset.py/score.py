# Take three subject marks from user (English, Math, Science). 
# Check if the student has passed: 
# All marks should be >= 40 (use 'and' operator) 
# If any one subject is < 40, print "Fail"

student = ['English','Math','Science']
a = 45
b = 37
c = 76
if a >= 40 and b>=40 and c>= 40:
    print("student has passed")    
else:
    print("student has failed")    