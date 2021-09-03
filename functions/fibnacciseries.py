limit=int(input("Enter the limit"))
first=0
second=1
for i in range (limit) :
    print(" ",first)
    next = first + second
    first=second
    second=next


