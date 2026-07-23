from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, color):
        self.__color = color

    def get_color(self):
        return f"Color : {self.__color}"

    def set_color(self, color):
        self.__color = color
        return "Color Updated"

    @abstractmethod
    def area(self):
        pass

    def shape_info(self):
        return f"Color : {self.__color}"


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.__radius = radius

    def area(self):
        area = 3.14 * self.__radius * self.__radius
        print(self.shape_info())
        print(f"Area : {area}")


circle = Circle("Red", 5)

print(circle.get_color())
print(circle.shape_info())
circle.area()