# Use reduce() with lambda to find the sum of all numbers.

from functools import reduce
lists = [10,20,30,40]

result = reduce(lambda x, y: x + y, [10,20,30,40])
print(result)

#Use reduce() with lambda to find the product of all numbers.
lists1 = [2,3,4,5]

result1 = reduce(lambda x,y : x*y,[2,3,4,5])
print(result1)