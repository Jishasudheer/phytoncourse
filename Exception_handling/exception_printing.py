lst=[45,2,3,6,78,74,50]
pos=int(input("Enter the position to display"))
try:
    print (lst[pos])
except Exception as e:
    print(e.args)
finally:
    print("executed finally")