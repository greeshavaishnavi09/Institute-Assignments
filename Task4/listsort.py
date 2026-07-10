# Create a tuple with 8 numbers. Find the index of the number 25. If it exists, count how many times it appears. Then convert the tuple into a list, sort it in descending order, and print.

tup = (25,67,54,25,86,95,25,9,18)
print(tup.index(25))
print(tup.count(25))
tup = list(tup)
tup.sort(reverse=True)
print(tup)
