lst=[56,45,89,75,23,12,14,-90,-67]
new_lst=[]

while lst:
    min = lst[0]
    for i in lst:
        if i < min :
            min = i
    new_lst.append(min)
    lst.remove(min)
print(new_lst)
print(lst)