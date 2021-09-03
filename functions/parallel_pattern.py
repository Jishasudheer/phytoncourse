def parallel(n):
    for i in range (n):
        for j in range (i):
            print(end=" ")

        for k in range(n):
            print("*",end=" ")
        print()

parallel(5)