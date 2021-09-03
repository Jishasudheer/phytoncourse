lst=[45,2,3,6,78,74,50]
pos=int(input("Enter the position to display"))
try:
    print (lst[pos])
except:
    print("out of index occured")