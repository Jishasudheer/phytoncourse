list1=[5,11,16,21,25,28]
list2=[4,5,10,11,16,20,23,28]
i=0
j=0
while(i<len(list1)):
    if(list1[i]==list2[j]):
        print(list1[i])
        i+=1
    elif(list1[i]<list2[j]):
        i+=1
    elif(list1[i]>list2[j]):
        j+=1


