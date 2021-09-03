def linear_search(ele):
    lst=[2,6,7,8,9,56,45,74,66,66,44]
    if ele in lst:
        print ("present")
    else:
        print("not present")
    # for i in (lst):
    #     if i == ele :
    #         print("Element is present",i)
    #         break
    # else:
    #     print("Element is not present")

element = int ( input("Enter the element to be searched"))
linear_search(element)