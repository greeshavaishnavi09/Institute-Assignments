class MathOperations:

    def multiply(self, *args):

        result = 1

        for i in args:
            result *= i

        return result


obj = MathOperations()

print(obj.multiply(2,3))
print(obj.multiply(2,3,4))
print(obj.multiply(2,3,4,5))
print(obj.multiply(2,3,4,5,6))