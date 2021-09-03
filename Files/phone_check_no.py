import re
f1=open("phonenumber","r")
x = "[+][9][1]\d{10}$"
for num in f1:
    n=num.rstrip("\n")
    match=re.fullmatch(x,n)
    if match != None:
        print(n)
