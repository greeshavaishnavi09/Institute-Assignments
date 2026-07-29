class Money:

    def __init__(self, amount):
        self.Amount = amount

    # Dunder Method : __add__
    def __add__(self, other):

        result = self.Amount + other.Amount

        return result

    # Dunder Method : __sub__
    def __sub__(self, other):

        result = self.Amount - other.Amount

        return result

    def __repr__(self):
        return f"Amount = {self.Amount}"

    def __str__(self):
        return f"Amount = {self.Amount}"

m1 = Money(1000)
m2 = Money(400)

print(m1)
print(m2)

print(m1 + m2)
print(m1 - m2)