min=int(input("Enter Minimum"))
max=int(input("Enter Maximum"))
if min>0:
    for i in range (min,max+1):
        if(i%2==0):
            print(" ",i)
else:
    print("Enter valid minimum value")


