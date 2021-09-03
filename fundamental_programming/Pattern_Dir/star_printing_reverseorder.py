n=int(input("Enter the rows"))
for i in range (n+1):
    for j in range (i,n+1):
        print ("*",end="..")
    print()
   # i=i-1