lst=[8,6,7,8,3,4,8,12,8,8]
dup=[]
count=1
for i in lst:
    if i not in dup:
        dup.append(i)
    else:
        count=count+1
print(count)
