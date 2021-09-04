list1=[10,12,23,45,74,11]
list2=[23,11,45,74,58,75]
common=[]
for i in list1:
    for j in list2:
        if(i==j and i not in common):
            common.append(i)
print(common)

