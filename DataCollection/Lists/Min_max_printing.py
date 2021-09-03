lst=[5,6,4,8,9,7,88,12,-8,91]
min=lst[0]
max=lst[0]
for i in lst:
    if min < i:
        max = i
    #elif (min > i):
    else:
        min = i
print("Minimum=",min)
print("Maximum=",max)
