def prime_no(min,max):
    sum=0
    flag=0
    if(min>=1):
        for i in range(min,max+1):
            for j in range(2,i):
                if(i%j==0):
                    break
            else:
                sum=sum+i
                #print(i)
    return(sum)

min=int(input("Enter the initial range"))
max=int(input("Enter the final range"))
print("Sum of Prime numbers=",prime_no(min,max))


