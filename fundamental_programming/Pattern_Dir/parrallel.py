row=5
for i in range (row):
    for j in range(row):
        print(end=" ")
    row=row-1
    for k in range (i+1):
        print("*",end=" ")
    print()