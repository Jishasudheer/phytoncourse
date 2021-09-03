class Bank:
    B_name="SBI"
    balance=5000
    def create_acc(self,name,address,type):
        self.name=name
        self.type=type
        self.address=address

    def deposite(self,amount):
        self.amount=amount
        Bank.balance=Bank.balance+self.amount
        print("Deposited")
        print("Balance=",Bank.balance)
    def withdrwal(self,with_amount):
        self.with_amount=with_amount
        if(self.with_amount>Bank.balance):
            print("Insufficient")
        else:
            self.with_amount=with_amount
            Bank.balance-=self.with_amount
            print("Current")
            print("Balance=",Bank.balance)


b1=Bank()
b1.create_acc("jisha","Mangalathu","Saving")
b1.deposite(10000)
b1.withdrwal(5000)
