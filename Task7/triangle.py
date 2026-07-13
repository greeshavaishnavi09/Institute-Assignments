#Take three sides of a triangle as input. First check if they can form a valid triangle (sum of any two sides > third side). If valid, then further check and print whether the triangle is Equilateral, Isosceles, or Scalene.

a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))


if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        print("Equilateral Triangle")
    else:
        if a == b or b == c or a == c:
            print("Isosceles Triangle")
        else:
            print("Scalene Triangle")
else:
    print("Invalid Triangle")