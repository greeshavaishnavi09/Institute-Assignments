def countdown():

	for i in range(20, 0, -1):
		yield i

gen = countdown()

for i in gen:
	print(i)