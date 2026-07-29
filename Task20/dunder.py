class Point:

    def __init__(self, x, y):
        self.X = x
        self.Y = y

    # Dunder Method : __add__
    def __add__(self, other):

        x = self.X + other.X 
        y = self.Y + other.Y

        return Point(x, y)

    def __repr__(self):
        result = f"Point(X = {self.X}, Y = {self.Y})"
        return result

    def __str__(self):
        result = f"Point(X = {self.X}, Y = {self.Y})"
        return result


p1 = Point(2, 3)
p2 = Point(5, 7)

print(p1)
print(p2)


p3 = p1 + p2

print(p3)

