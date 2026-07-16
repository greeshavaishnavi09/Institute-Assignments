# 1. Combined Functions + List Comprehension Write a single line of code using list comprehension + built-in functions to:

 #Take numbers from 1 to 50
 #Keep only numbers that are divisible by both 3 and 5
 #Convert them to strings
 #Add " (multiple)" at the end of each
 #Return the final list


result = [f"{num} (multiple)" for num in range(1,51) if(num %3 ==0 and num %5 == 0)]
print(result)