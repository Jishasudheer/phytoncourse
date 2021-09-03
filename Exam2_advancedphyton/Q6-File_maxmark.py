f=open('mark','r')
min=0
max=0
for i in f:
    lst=i.split(" ")
    for j in lst:
        each=j.split(",")
        if max<int(each[3]):
                max=int(each[3])
print(max)




# max=each[0]
# for i in lst:
#     if min < i:
#         max = i
#     #elif (min > i):
#     else:
#         min = i
# print("Minimum=",min)
# print("Maximum=",max)



