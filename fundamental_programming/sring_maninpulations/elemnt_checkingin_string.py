str="jisha"
flag=0
c=input("enter an element to check")
for i in str:
    if i in c:
        print("Element is  present")
        flag=0
        break
    else:
        flag=1
if(flag==1):
    print("Element is not present")
