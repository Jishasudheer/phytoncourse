r1=int(input("Enter initial range"))
r2=int(input("Enter final range"))
for i in range (r1,r2+1):
    if(i%2!=0):
        for j in range(0,r2):
            for k in range(j+1):
                print(i,end=" ")
            print()
    else:
        for j in range(r2,0,-1):
            for k in range (j):
                print(i,end=" ")
            print()
