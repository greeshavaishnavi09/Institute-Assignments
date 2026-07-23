#  payments 
from abc import ABC, abstractmethod

class Payments(ABC):
    def __init__(self,owner,amount):
        self.__owner_name=owner
        self.__amount = amount

    def get_owner_name(self):
        return f"owner:{self.__owner_name}"

    def get_amount(self):
            return f"amount:{self.__amount}"

    def set_amount(self,amt):
         if amt>0:
              self.__amount+=amt
              return f" amount updated:{self.__amount}"
         else:
              print("please enter the amount more than zero")

    #abstractmethods :

    @abstractmethod
    def pay(self):
         pass

    # instance methods
    def  recepit(self):
         print(f"owner:{self.__owner_name}")
         print(f"amount:{self.__amount}")         

# child class
class Credit_card(Payments):
     def __init__(self,owner,amount,credit_card_no):
        super().__init__(owner,amount)
        self.__credit_card = credit_card_no

     def pay(self):
          print("credit card details:")
          print("credit card number:{self.__credit_card}")  
          self.recepit()

credit = Credit_card("Greesha",500,345678)

print(credit.get_owner_name())
print(credit.get_amount())
print(credit.recepit())
print(credit.pay())
