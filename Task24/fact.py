def factors(num):

	for i in range(1, num + 1):

		if num % i == 0:
			yield i

gen = factors(24)

for i in gen:
	print(i)