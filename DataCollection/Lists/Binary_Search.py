# Binary Search

lst=[56,45,78,89,12,23,78,91,54]
def Binary_Search(lst):
    element=int(input("Enter the element"))
    flag=0
    lst.sort()
    first=0
    last=len(lst)-1
    while first <= last :
        mid=(first+last)//2
        if lst[mid]==element:
            print("Element found")
            flag=1
            break
        elif lst[mid]>element:
            last=mid-1
        else:
            first=mid+1
    if flag == 0:
        print("Element not found")

Binary_Search(lst)