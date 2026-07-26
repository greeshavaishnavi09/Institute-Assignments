class MathUtils:
    def __init__(self, precision, **kwargs):
        super().__init__(**kwargs)
        self.__precision = precision

    def get_precision(self):
        return self.__precision

    def set_precision(self, precision):
        self.__precision = precision

    @staticmethod
    def add(a, b):
        return a + b


class AdvancedMath(MathUtils):
    def __init__(self, precision, algorithm_name, **kwargs):
        super().__init__(precision=precision, **kwargs)
        self.__algorithm_name = algorithm_name

    def get_algorithm_name(self):
        return self.__algorithm_name

    def set_algorithm_name(self, name):
        self.__algorithm_name = name

    @staticmethod
    def multiply(a, b):
        return a * b


# Execution and Verification
math_obj = AdvancedMath(precision=4, algorithm_name="Matrix Multiplication")


print("Parent Static (add):", AdvancedMath.add(10, 5))
print("Child Static (multiply):", AdvancedMath.multiply(10, 5))
print("Algorithm Name:", math_obj.get_algorithm_name())
