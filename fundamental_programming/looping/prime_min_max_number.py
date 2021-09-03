min=int(input("Enter Minimum"))
max=int(input("Enter Max"))
for i in range (min,max+1):
    for j in range (2,i):
        if i%j==0:
            break
    else:
        print (i)