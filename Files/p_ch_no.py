import re
f=open("phonenumber",'r')
for num in f:
    n=num.rstrip("\n")
    x="[+][9][1]\d{10}$"
    match=re.fullmatch(x,n)
    if match is not None:
        print(n)
