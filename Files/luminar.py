import re
f1=open("lumin",'r')
for i in f1:
    word=i[5]+i[6]
    match = re.fullmatch("PY",word)
    if match is not None:
        print(i)

