
try:
    balance = 5000
    deposit = int(input("Enter Deposit Amount: "))
    balance = balance + deposit

    print("Balance After Deposit:", balance)

    withdraw = int(input("Enter Withdraw Amount: "))

    if withdraw > balance:
        raise Exception("Insufficient Balance")

    balance = balance - withdraw

    print("Balance After Withdraw:", balance)

except Exception as e:
    print(e)

except ValueError:
    print("Enter valid amount.")