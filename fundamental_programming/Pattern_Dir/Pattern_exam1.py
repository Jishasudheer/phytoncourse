r1=int(input("Enter initial range"))
r2=int(input("Enter final range"))
no=0
while(no<r2):
    no=no+1
    for i in range(r2+1):
        for j in range (i):
            print(no,end=" ")
        print()
    no = no + 1
    for i in range(r2):
        for k in range (i,r2):
            print(no,end=" ")
        print()