# Take your city name as input. 
# Print the following: 
# 1. City name in reverse order 
# 2. Number of vowels in the city name (a,e,i,o,u) 
# 3. City name without first and last character 

name = "Hyderabad"
reversed_name = ""
vow = "aeiou"
count = 0
for char in name:
    reversed_name = char+ reversed_name
print(reversed_name)    
 
for char in name:
    if char in vow:
        count+=1
        print(count)       

if char in name:
    print(name[1:-1])
else:
    print(None)    

