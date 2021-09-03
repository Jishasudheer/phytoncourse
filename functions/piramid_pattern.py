def piramid(n):
    for i in range (n):
        for j in range(n):
            print (end=" ")
        n=n-1
        for k in range (i+1):
                print ("*",end=" ")
        print()

piramid(6)