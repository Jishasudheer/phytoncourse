list1=[11,16,21,25,27]
list2=[12,16,20,21,28]
l1=len(list1)
l2=len(list2)
i=0
j=0
while(l1<=l2):
    if(list1[i]==list2[j]):
        print(list1[i])
        break
    elif(list1[i]<list2[j]):
        i+=1
    elif(list1[i]>list2[j]):
        j+=1


