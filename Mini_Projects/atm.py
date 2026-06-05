print("ATM STSTEM")

balance = 5000
amount = int(input("Enter Withdraw Amount: "))

if amount <= balance:
    print("Transactions Successful")
    print("Remaining Balance =", balance - amount)

else:
    print("Insufficient Balance")