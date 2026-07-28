import math

class Circle:
    def __init__(self,r):
        self.r = r

    def draw(self):
        print("Drawing a circle")

    def area(self):
        print("area of circle", math.pi* self.r **2 )

class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def draw(self):
        print("Drawing a Rectangle")

    def area(self):
        print("area of Rectangle", self.width* self.height ) 


class Triangle:
    def __init__(self,base,height):
        self.base = base
        self.height = height

    def draw(self):
        print("Drawing a Triangle")

    def area(self):
        print("area of Triangle", 0.5 * self.base * self.height ) 


def display(shape):
    shape.draw()
    shape.area()   


c = Circle(3)
r = Rectangle(4,6)
t = Triangle(4,5)

display(c)
display(r)
display(t)
