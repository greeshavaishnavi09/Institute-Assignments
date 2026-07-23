from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return f"Balance : {self.__balance}"

    def set_balance(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Updated Balance : {self.__balance}"
        else:
            print("Invalid Amount")

    @abstractmethod
    def calculate_interest(self):
        pass

    def account_info(self):
        return f"Balance : {self.__balance}"


class SavingsAccount(BankAccount):
    def __init__(self, balance, rate):
        super().__init__(balance)
        self.__rate = rate

    def calculate_interest(self):
        interest = self._BankAccount__balance * self.__rate / 100
        print(f"Interest : {interest}")


account = SavingsAccount(50000, 5)

print(account.get_balance())
print(account.account_info())
account.calculate_interest()