import re
flag=0

f1=open("phonenumber",'r')
for i in f1:
    x = "[+][9][1]\d{10}$"
    number=i.rstrip("\n")
    match = re.fullmatch(x,number)
    if match!=None:
        print(i)


