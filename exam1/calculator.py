def addition(n1,n2):
    sum=n1+n2
    print("Sum=",sum)
def subtraction(n1,n2):
    diff=n1-n2
    print("Difference=",diff)
def Multipliction(n1,n2):
    mult=n1*n2
    print("Product=",mult)
def division(n1,n2):
    if(n2==0):
        print("Division by zero is not possible")
    else:
        div=n1/n2
        print("Quoificient=",div)
def floor_division(n1,n2):
    if(n2==0):
        print("Division by zero is not possible")
    else:
        f_div=n1//n2
        print("Floor_division result=",f_div)
def expone(n1,n2):
    exp=n1**n2
    print("Exponent result=",exp)

print("1.Addition 2.Subtraction 3.Multiplication")
print("4.Division 5.Floor division 6.Exponent ")
print("7.Exit")
n1=int(input("Enter number1"))
n2=int(input("Enter number2"))
c=int(input("Enter ypur choice"))
while True:
    if c<=0 or c>=8:
        print("Invalid choice")
        print("Enter a valid choice")
        break
    elif(c==1):
        addition(n1,n2)
        break
    elif(c==2):
        subtraction(n1,n2)
        break
    elif(c==3):
        Multipliction(n1,n2)
        break
    elif (c==4):
        division(n1, n2)
        break
    elif(c==5):
        floor_division(n1, n2)
        break
    elif(c==6):
        expone(n1, n2)
        break
    elif(c==7):
        break
