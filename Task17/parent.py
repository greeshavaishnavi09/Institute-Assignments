class Parent1:
    def __init__(self, p1_val, **kwargs):
        super().__init__(**kwargs)
        self.__p1_val = p1_val

    def get_p1_val(self):
        return self.__p1_val

    def set_p1_val(self, val):
        self.__p1_val = val

    @staticmethod
    def parent1_greet():
        return "Hello from Parent1 static method!"


class Parent2:
    def __init__(self, p2_val, **kwargs):
        super().__init__(**kwargs)
        self.__p2_val = p2_val

    def get_p2_val(self):
        return self.__p2_val

    def set_p2_val(self, val):
        self.__p2_val = val

    @staticmethod
    def parent2_greet():
        return "Hello from Parent2 static method!"


class Child(Parent1, Parent2):
    def __init__(self, p1_val, p2_val, child_val, **kwargs):
        super().__init__(p1_val=p1_val, p2_val=p2_val, **kwargs)
        self.__child_val = child_val

    def get_child_val(self):
        return self.__child_val

    def set_child_val(self, val):
        self.__child_val = val

    @staticmethod
    def child_greet():
        return "Hello from Child static method!"


# Execution and Verification
obj = Child(p1_val="P1 Data", p2_val="P2 Data", child_val="Child Data")


print("Parent1 :", Child.parent1_greet())
print("Parent2 :", Child.parent2_greet())
print("Child :", Child.child_greet())
print("P1 Value:", obj.get_p1_val())
