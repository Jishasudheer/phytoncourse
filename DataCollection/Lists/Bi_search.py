def Bi_searh(lst,ele):
    first=0
    lst.sort()
    last=len(lst)
    flag=0
    while(first<=last):
        mid=(first+last)//2
        if(lst[mid]== ele):
             flag=1
             print(mid)
             break
        elif(lst[mid]<ele):
            first=mid+1
            flag=0
        elif(lst[mid]>ele):
            last=mid-1
            flag=0
    if(flag==0):
        print("Not found")
    else:
        print("Found")

lst=[12,32,41,3,86,95,4,74,47,53]
ele=int(input("Enter the element to be searched"))
Bi_searh(lst,ele)
