fixed_amount=10000
withdraw_amount=int(input("Enter the amount for withdrwal"))
if fixed_amount< withdraw_amount :
     print("Insufficient")
else :
    balance=fixed_amount-withdraw_amount
    print("Balance=",balance)