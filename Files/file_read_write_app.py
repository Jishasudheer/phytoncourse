f1=open("samplet",'r+')
f1.write("jisha")
f1.write("\n")
f1.write("sudhi")
f1.write("\n")
for i in f1:
     print(i)
f3=open("samplet",'a')
f3.write("Eshwar")
f3.write("\n")
f3.write("Adya")
f3.close()
f4=open("samplet",'r')
for i in f4:
    print(i)

