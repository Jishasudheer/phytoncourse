age=int(input("Enter age"))
if age<18 :
    raise Exception("Not eligible for vaccine")
else :
    print("vaccine available")