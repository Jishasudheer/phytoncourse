n1=int(input("Enter no1"))
n2=int(input("Enter no2"))
try:
    div=n1/n2
    print (div)
except Exception as e:
    print(e.args)
finally:
    print("Finally executed")