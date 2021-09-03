n1=int(input("Enter no1"))
n2=int(input("Enter no2"))
if n2>n1:
    raise Exception("No2 greater than no1")
else:
    print(n1/n2)