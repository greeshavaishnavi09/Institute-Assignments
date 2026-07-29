class Shape:

    def __init__(self, name):
        self.Name = name

    def area(self):
        print(f"{self.Name} Area")


class Circle(Shape):

    def __init__(self, name, radius):
        super().__init__(name)
        self.Radius = radius

    def area(self):

        circle_area = 3.14 * self.Radius * self.Radius

        print(f"{self.Name} Area : {circle_area}")


class Rectangle(Shape):

    def __init__(self, name, length, width):
        super().__init__(name)
        self.Length = length
        self.Width = width

    def area(self):

        rectangle_area = self.Length * self.Width

        print(f"{self.Name} Area : {rectangle_area}")


cir = Circle("Circle", 5)
rec = Rectangle("Rectangle", 10, 4)

cir.area()
rec.area()