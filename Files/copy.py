f1=open('content','r')
f2=open('copycontent','w')
for i in f1:
   print(i)
   f2.write(i)
f2.close()
f1.close()
f3=open('copycontent','a')
f3.write('ki')


