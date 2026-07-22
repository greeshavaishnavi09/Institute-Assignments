class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = 0
        if initial_balance > 0:
            self.__balance = initial_balance

    def display_all_details(self):
        print(f"Current Balance: {self.__balance}")

    # --- Deposit Method ---
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Successfully deposited: {amount}")
        else:
            print("Deposit amount must be greater than 0.")

    # --- Withdraw Method ---
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
        elif amount > self.__balance:
            print("Insufficient balance! Withdrawal rejected.")
        else:
            self.__balance -= amount
            print(f"Successfully withdrew: {amount}")

    def get_balance(self):
        return self.__balance



account = BankAccount(1000)
account.deposit(500)
account.withdraw(300)
account.withdraw(2000)  # Invalid: overdrawing
account.display_all_details()
