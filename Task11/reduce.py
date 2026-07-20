# Use reduce() with lambda to find the sum of all numbers.

from functools import reduce
lists = [10,20,30,40]

result = reduce(lambda x, y: x + y, [10,20,30,40])
print(result)