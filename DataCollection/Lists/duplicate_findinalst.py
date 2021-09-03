lst=[4,5,8,9,4,6,7,2]
dup=[]
j=0
#common=lst[0]
for i in lst:
    if i not in dup:
        dup.append(i)
    else:
        print(i)
