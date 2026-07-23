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


class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.__length = length
        self.__width = width

    def area(self):
        area = self.__length * self.__width
        print(self.shape_info())
        print(f"Area : {area}")


rect = Rectangle("Blue", 10, 5)

print(rect.get_color())
print(rect.shape_info())
rect.area()