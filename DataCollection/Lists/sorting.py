lst=[12,45,89,52,11,9,46]
new_list=[]
while lst:
    min=lst[0]
    for i in lst:
        if i<min :
            min=i
    new_list.append(min)
    lst.remove(min)
print (new_list)