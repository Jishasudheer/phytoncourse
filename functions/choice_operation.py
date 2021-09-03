
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y


while True:
    print("Select operation")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    choice = int(input("Enter your choice"))
    if choice == 5:
       break
    if(choice <1 or choice>5):
        print("Invalid")
        print("Enter a Valid option")
        continue
    num1=int(input("Enter the number1\n"))

    num2=int(input("Enter the number2\n"))
    if choice == 1:
            print(add(num1,num2))
    elif choice==2:
            print(subtract(num1,num2))
    elif choice==3:
            print(multiply(num1,num2))
    elif choice==4:
            print(divide(num1,num2))







