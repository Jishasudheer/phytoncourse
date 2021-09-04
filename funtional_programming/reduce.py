from functools import reduce
lst=[2,5,4,6]
total=reduce(lambda n1,n2:n1+n2,lst)
print(total)

highest_num=reduce(lambda n1,n2:n1 if n1>n2  else n2,lst)
print(highest_num)

lowest_num=reduce(lambda n1,n2:n1 if n1<n2 else n2,lst)
print(lowest_num)

# n=int(input("Enter number"))
# print("negative" if n<0 else "positive")

