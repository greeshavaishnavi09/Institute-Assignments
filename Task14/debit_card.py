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

    #abstractmethod :

    @abstractmethod
    def pay(self):
         pass

    # instance methods
    def  recepit(self):
         return f"owner:{self.__owner_name} \n amount:{self.__amount}"
                 

# child class
class Credit_card(Payments):
     def __init__(self,owner,amount,credit_card_no):
        super().__init__(owner,amount)
        self.__credit_card = credit_card_no

     def pay(self):
               print("credit card details:")
               print(f"credit card number:{self.__credit_card}")  
               self.recepit()


class Debit_card(Payments):
     def __init__(self,owner,amount,debit_cardno):
        super().__init__(owner,amount)
        self.__Debit_card = debit_cardno
     def pay(self):
               print("Debit card details:")
               print(f"Debit card number:{self.__Debit_card}") 
               self.recepit()   

class UPI_no(Payments):
     def __init__(self,owner,amount,upi_no):
             super().__init__(owner,amount)
             self.__upi_no = upi_no

     def pay(self):
               print("upi details:")
               print(f"upi number:{self.__upi_no}")  
               self.recepit()        
       

     
credit = Credit_card("Sumit",500,345678)
debit = Debit_card("Greesha",4000,5678)
upi = UPI_no("Vaishnavi",4569,5678)

print(credit.get_owner_name())
print(credit.get_amount())
print(credit.recepit())
print(credit.pay())

print(debit.get_owner_name())
print(debit.get_amount())
print(debit.recepit())
print(debit.pay())

print(upi.get_owner_name())
print(upi.get_amount())
print(upi.recepit())
print(upi.pay())



