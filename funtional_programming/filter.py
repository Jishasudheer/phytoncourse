# fiter(function,list/dict)
# check even
lst=[1,5,4,6,8]
def even(num):
    return(num%2==0)
print(list(filter(even,lst)))

even=list(filter(lambda num:num%2==0,lst))
print(even)

odd=list(filter(lambda num:num%2!=0,lst))
print(odd)