class BankAccount:

    def __init__(self, account_holder):
        self.AccountHolder = account_holder

    def interest(self):
        print(f"{self.AccountHolder} Interest : 2%")


class SavingsAccount(BankAccount):

    def interest(self):
        print(f"{self.AccountHolder} Savings Interest : 6%")


class CurrentAccount(BankAccount):

    def interest(self):
        print(f"{self.AccountHolder} Current Interest : 3%")


saving = SavingsAccount("Vaishnavi")
current = CurrentAccount("Priya")

Accounts = [saving, current]

for account in Accounts:
    account.interest()