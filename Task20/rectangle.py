class Rectangle:

    def __init__(self, length, width):
        self.Length = length
        self.Width = width

    # Dunder Method : __eq__
    def __eq__(self, other):

        area1 = self.Length * self.Width
        area2 = other.Length * other.Width

        return area1 == area2

    def __repr__(self):
        return f"Rectangle(Length = {self.Length}, Width = {self.Width})"

    def __str__(self):
        return f"Rectangle(Length = {self.Length}, Width = {self.Width})"


r1 = Rectangle(4, 5)
r2 = Rectangle(2, 10)

print(r1)
print(r2)

print(r1 == r2)