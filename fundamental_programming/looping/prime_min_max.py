min=int(input("Enter the minimum Value"))
max=int(input("Enter the Maximum Number"))
flag=0
for i in range (min,max+1):
      for j in range (2,i):
          if(i%j==0):
            flag=0
            break
          else:
            flag=1
      if(flag==1):
          print (i)

