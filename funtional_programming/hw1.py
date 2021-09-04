# lst=[2,4,8] [10,8,6]
# lst=[3,5,7] [12,10,8]
# lst1=[2,4,6]
# lst2=
lst=[3,5,7]
total=sum(lst)
op=[total-n for n in lst]
print(op)

# print(list(map(lambda n:sum(lst1)-n,lst1)))
# print(list(map(lambda n:sum(lst2)-n,lst2)))

#Sum of pairs
lst=[]
# lst=[2,3,4,5] 6(4,2)(3,3)(1,5)
lst=[2,3,4,5,6]
pair=8
pairs=[]
low=0
upp=len(lst)-1
while(low<upp):
   sum=lst[low]+lst[upp]
   if (sum==pair):
      pairs.append((lst[low],lst[upp]))
      low+=1
   elif(sum>pair):
      upp-=1
   elif(sum<pair):
      low+=1
print(pairs)




# lst=[2,3,4,5]
# print(tuple(map(lambda n:)))