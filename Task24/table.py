table = []

for i in range(1, 11):
	table.append(5 * i)

it = iter(table)

for i in it:
	print(i)