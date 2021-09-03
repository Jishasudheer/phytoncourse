lst=[1,0,7,5,9,2,3,5,7,2,0,1,10]
# dup=list(set(lst))
dup=[]
[dup.append(x) for x in lst if x not in dup]
print (dup)



# dup=[]
# dup.append(i for i in lst if i not in dup)
# print(dup)

# lst=[1,0,7,5,9,2,3,5,7,2,0,1,10]

# dup=[]
#dup=[i for i in lst if i!=dup]
# for i in lst:
#    if i not in dup:
#        dup.append(i)
# print (dup)
