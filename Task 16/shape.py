class Shape:

    # Constructor

    def __init__(self, color):
        self.__color = color

    # Getter

    def get_color(self):
        return f"Color : {self.__color}"

    # Setter

    def set_color(self, color):
        self.__color = color
        print("Color Updated")

    # Parent Method

    def area(self):
        print("Area of Shape")

    def shape_info(self):
        return f"Color : {self.__color}"


# Child Class

class Circle(Shape):

    # Constructor

    def __init__(self, color, radius):
        super().__init__(color)
        self.__radius = radius

    # Getter

    def get_radius(self):
        return f"Radius : {self.__radius}"

    # Setter

    def set_radius(self, radius):
        self.__radius = radius
        print("Radius Updated")

    # Method Overriding

    def area(self):
        area = 3.14 * self.__radius * self.__radius
        print(f"Area of Circle : {area}")

    # Child Method

    def circle_info(self):
        print(self.shape_info())
        print(f"Radius : {self.__radius}")

circle = Circle("Red", 7)

print(circle.get_color())
print(circle.get_radius())

circle.circle_info()
circle.area()

