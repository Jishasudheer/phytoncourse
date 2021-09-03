import re

x='[0-9]{2}[k][g]'
n="50kg"
match=re.fullmatch(x,n)
if match is not None:
    print("Valid")
else:
    print("not valid")