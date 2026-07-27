class Shape:

    # Parent Method
    def area(self):
        print("Calculating Area")


class Circle(Shape):

    def __init__(self):
        super().__init__()


class Rectangle(Shape):

    def __init__(self):
        super().__init__()


c1 = Circle()
r1 = Rectangle()

print("Circle")
c1.area()

print("Rectangle")
r1.area()