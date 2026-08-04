numbers = [10, 20, 30]

iterator = iter(numbers)

try:
	print(next(iterator))
	print(next(iterator))
	print(next(iterator))
	print(next(iterator))
except StopIteration:
	print("No more elements in the iterator")