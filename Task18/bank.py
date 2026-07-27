class Bankaccount:

    # Parent Method
    def deposit(self):
        print("Amount deposited")


class Savingsaccount(Bankaccount):

    def __init__(self):
        super().__init__()


class Currentaccount(Bankaccount):

    def __init__(self):
        super().__init__()


sa = Savingsaccount()
ca = Currentaccount()

print("Savingsaccount")
sa.deposit()

print("Currentaccount")
ca.deposit()