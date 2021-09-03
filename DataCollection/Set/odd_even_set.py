s={2,7,5,4,3,78,98,67,55,23,14}
odd=set()
even=set()
for i in s:
    if i % 2 == 0:
        odd.add(i)
    else:
        even.add(i)
print("odd set is")
print(odd)
print("Even set is")
print(even)
