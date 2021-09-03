f1=open('Sample','w')
f1.write("Hello...We wrote hello in the file sample")
f1.close()
f2=open('Sample','r')
for i in f2:
    print (i)