import re
file1=open("phone","r")
file2=open("create",'w')
x = "[+][9][1]\d{10}$"
for num in file1:
    onenum=num.rstrip("\n")
    match=re.fullmatch(x,onenum)
    if match is not None:
        file2.write(onenum+"\n")





