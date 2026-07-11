# Take three numbers. Print them in ascending order using if-elif-else (without using sort()).

a = 1
b = 3
c = 4

if a<=b and b<=c and a<=c:
    print("ascending order")
elif a>=b and b>=c and a>=c:
    print("not an ascending order")
else:
    print("none")
          