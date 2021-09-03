set1={1,3,5,7,8,9,56,67}
set2={3,6,4,8,12,67,56}
common = set()
for i in set1:
    if i in set2:
         common.add(i)
print(common)