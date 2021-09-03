class Bank:
    name="SBI"
    balance=5000
    def __init__(self,name,age,type):
        self.name=name
        self.age=age
        self.type=type
    def deposite(self,amount):
        Bank.balance+=amount
        print(amount,"is deposited")
    def withdrwal(self,amount):
        if amount>Bank.balance:
            print("Insufficient")
        else:
            Bank.balance-=amount
            print("Current balance=",Bank.balance)
    def balancecheck(self):
        print("Your balance=",Bank.balance)
# class Person(Bank):
#     def __init__(self,name1,address):
#         self.name1=name1
#         self.address=address
#         super().__init__(self,name,age,type,name1,address)

b=Bank("Jisha",36,"savings account")
while(True):
    print("1.deposite  2.withdrwal  3.balance checking  4.Exit")
    ch=int(input("Enter your choice"))
    if(ch==4):
        break
    if(ch<=0 and ch>4):
        print("Enter a Valid choice")
    while(ch<=3):
        if ch==1:
            amount=int(input("Enter the Amount to deposite"))
            b.deposite(amount)
            break
        if ch==2:
            amount=int(input("Enter the amount to be withdraw"))
            b.withdrwal(amount)
            break
        if ch==3:
            b.balancecheck()
            break
