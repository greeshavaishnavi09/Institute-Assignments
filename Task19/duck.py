class Creditcard:
    def pay(Self,amount):
        return f"paying amount using credit card:{amount}"

class Debitcard:
    def pay(Self,amount):
        return f"paying amount using Debit card:{amount}"  

class Upi:
    def pay(Self,amount):
        return f"paying amount using Upi:{amount}"      
# make function
def make_payement(payement,amount):
    payement.pay(amount) 

# create objects

c= Creditcard()
d= Debitcard()
u = Upi()

make_payement(c,500)
make_payement(d,500)
make_payement(u,500)

print(c.pay(100))
print(d.pay(500))
print(u.pay(300))



