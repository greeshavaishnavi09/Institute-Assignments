class Account:
    def __init__(self, user, account_number, balance):
        self.user = user
        self.__account_number = account_number  
        self.balance = balance                  

    def display_account_info(self):
        masked_number = f"XXXX-XXXX-{str(self.__account_number)[-4:]}"
        return f"user: {self.user}, Account: {masked_number}, Balance: {self.balance}"
    
acc = Account("Greesha", 9876543210, 5000)
print(acc.display_account_info())
