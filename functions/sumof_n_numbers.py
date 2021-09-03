def sumofnnumbers(num):
    s=0
    for i in range (num+1):
        s=s+i
    print("Sum of n numbers=",s)

limit=int(input("Enter the limit"))
sumofnnumbers(limit)