class Calculator:
    def __init__(self,n1,n2):
            self.n1=n1
            self.n2=n2
    def add(self):
        print("Sum=",self.n1+self.n2)
    def subtraction(self):
        print("Difference=",self.n1-self.n2)
    def multiplication(self):
        print("Product=",self.n1*self.n2)
    def division(self):
        print("Quioficient= ",self.n1/self.n2)

while True:
    print("1.Addition")
    print("2.Subtraction")
    print("3.multiplication")
    print("4.Division")
    print("5.Exit")
    ch=int(input("Enter your choice"))
    if(ch==5):
        break
    elif(ch>=6 or ch<=0):
        print("Invalid choice....Please enter a valid choice")
    elif ch==1:
        n1 = int(input("Enter first number"))
        n2 = int(input("Enter second number"))
        c1=Calculator(n1,n2)
        c1.add()

    elif ch==2:
        n1 = int(input("Enter first number"))
        n2 = int(input("Enter second number"))
        c1=Calculator(n1,n2)
        c1.subtraction()

    elif ch==3:
        n1 = int(input("Enter first number"))
        n2 = int(input("Enter second number"))
        c1=Calculator(n1,n2)
        c1.multiplication()

    elif ch==4:
        n1=int(input("Enter first number"))
        n2=int(input("Enter second number"))
        try:
             c1=Calculator(n1,n2)
             c1.division()
        except Exception as e:
            print(e.args)




