str=input("Enter a String")
che=input("Enter the element")
count=0
for i in str:
    if i in che:
        count=count+1
print("Count=",count)
