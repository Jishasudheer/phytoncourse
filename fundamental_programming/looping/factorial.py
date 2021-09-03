num=int(input("Enter a number"))
f=1
if( num<0):
    print("Doesnt exist for -ve number")
else:
    for i in range (1,num+1):
        f=f*i
    print("factorial =",f)
