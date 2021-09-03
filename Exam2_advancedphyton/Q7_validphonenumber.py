import re
f=open("phonenumber",'r')
x = "[+][9][1]\d{10}$"
for num in f:
    n=num.rstrip("\n")
    match=re.fullmatch(x,n)
    if match != None:
        print(n)

