# n1=int(input("Enter the number"))
# n2=int(input("Enter the second number"))
# try:
#     print(n1/n2)
# except Exception as e:
#     print(e.args)
# finally:
#     print("Successfull operation/Unsuccessfull")
age=int(input("Enter age"))
if age<18:
    raise Exception("Not eligible for vaccine")
else:
    print("elegible for vaccine")