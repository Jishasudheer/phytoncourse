lst=[2,4,5,7]

evens=list(filter(lambda num:num%2==0,lst))
print(evens)

odds=list(filter(lambda num:num%2!=0,lst))
print(odds)