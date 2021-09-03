#Printing the employee record having sal above 15000
lst=[(1,"anu",28,20000),(2,"Bini",35,15000),(3,"ram",25,10000)]
for tup in lst:
    if tup[-1] >= 15000:
        print(tup)
    