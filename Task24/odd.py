def odd():
    for i in range(1, 20, 2):
        yield i

gen = odd()

for i in gen:
    print(i)