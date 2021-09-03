set1={1,2,3,4,5,6,9,8,7,11,12,13,14,15,16,75,48}
prime = set()
notprime = set()
for i in set1:
   if i >= 1:
      for j in range(2, i):
        if i % j == 0:
            notprime.add(i)
            break
      else :
          prime.add(i)
print(prime)
print(notprime)