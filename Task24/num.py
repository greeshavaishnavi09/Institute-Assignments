def numbers():

	for i in range(1, 11):
		yield i

gen = numbers()

for i in gen:
	print(i)