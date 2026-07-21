# bank management

class Bank_management:
    bank_name = "State Bank Of India"   # class variable
    def __int__(self,ac_no,bal,branch):
        self.Account_number=ac_no
        self.Balance = bal
        self.Branch = branch

    def display_bank_details(self):
        print(f"Account_number: {self.Account_number}, Balance: {self.Balance}, branch: {self.Branch},Bank_management:"bank_name"")
    def deposit_money(self,amt):  
        if amt>0:
            self.Balance+=amt
            print(f"{self.Balance}succesfully Done!")
        else:
            print("please enter the amount greater than zero")    
    def withdraw_money(self,amt):
        if amt > 0:
            if amt <= self.Balance:
                self.amount -=amt 
                print(f"withdraw money {amt}succesfully Done!") 
            else:
                print("Insuffient balnace {self.Balance}")

        else:
            print("please enter the amount greater than zero")  
          

bank = Bank_management(12345,20000,"medchal")
bank.deposit_money(10000)
bank.withdraw_money(20000)
bank.display_bank_details()




