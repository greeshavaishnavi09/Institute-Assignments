class Book:

    def __init__(self, pages):
        self.Pages = pages

    # Dunder Method : __add__
    def __add__(self, other):

        total_pages = self.Pages + other.Pages

        return total_pages

    def __repr__(self):
        return f"Book(Pages = {self.Pages})"

    def __str__(self):
        return f"Book(Pages = {self.Pages})"


# Class Objects
b1 = Book(250)
b2 = Book(300)

print(b1)
print(b2)

print( b1 + b2)