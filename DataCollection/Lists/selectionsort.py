def selectionsort(lst):
    new_lst=[]
    while lst:
        min=lst[0]
        for i in lst:
            if i < min:
                min=i
        new_lst.append(min)
        lst.remove(min)
    print(new_lst)

lst=[23,45,-78,-56,4,9,77,44]
selectionsort(lst)
