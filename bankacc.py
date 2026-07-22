class BankAccount:
    def __init__(self, balance=0.0):
        self.__balance = balance
        
    def get_balance(self):
        return self.__balance
        
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Error: Balance cannot be negative.")
    def display_details(self):
        print(f"balance:{self.__balance}")         

bank = BankAccount(4000)
print(bank.get_balance())

bank.set_balance(3000)
print(bank.get_balance())

bank.display_details()
