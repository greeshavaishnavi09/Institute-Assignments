# Attributes customer_name cart_total wallet_balance
# Methods
# add_item(price)
# remove_item(price)
# checkout()

# Cart total cannot become negative.
# Checkout only if wallet balance is enough.
# Deduct wallet balance after successful checkout.
# Cart becomes zero after payment.
# print suitable messages for every case.

class Online_shopping():

    def __init__(self,customer_name ,cart_total ,wallet_balance):
        self.customer_name = customer_name 
        self.cart_total = cart_total
        self.wallet_balance = wallet_balance

    def display_details(self):
        print(f"Customer_name: {self.customer_name},cart_total : {self.cart_total}, wallet_balance: {self.wallet_balance}")
    
    def add_items(self,price):
        if price <= 0:
            print("[Error] Item price must be greater than zero.")
            return
        self.cart_total += price
        print(f"[Success] Added item worth {price}. New cart total: {self.cart_total}")

    def remove_items(self,price):
        if price <= 0:
            print("[Error] Item price must be greater than zero.")
            return
        # Check condition: Cart total cannot become negative
        if self.cart_total - price < 0:
            print(f"[Error] Cannot remove {price}. Cart total cannot fall below 0 (Current cart: {self.cart_total}).")
        else:
            self.cart_total -= price
            print(f"[Success] Removed item worth {price}. New cart total: {self.cart_total}") 

    def checkout(self):
        if self.cart_total == 0:
            print("[Notice] Your cart is empty! Add items before checking out.")
            return

        print(f"\n[Checkout] Attempting to purchase items worth {self.cart_total}")

        # Check condition: Checkout only if wallet balance is enough
        if self.wallet_balance >= self.cart_total:
            self.wallet_balance -= self.cart_total  # Deduct wallet balance
            print(f"[Success] Payment complete! Deducted ₹{self.cart_total} from your wallet.")
            self.cart_total = 0                     # Cart becomes zero after payment
            print(f"Remaining Wallet Balance: ₹{self.wallet_balance}")
        else:
            shortfall = self.cart_total - self.wallet_balance
            print(f"[Decline] Insufficient wallet balance! You need ₹{shortfall} more to complete this transaction.")

shop = Online_shopping("Greesha",2500,1000)

shop.display_details()
shop.add_items(500)
shop.remove_items(1000)
shop.checkout()
shop.display_details()
