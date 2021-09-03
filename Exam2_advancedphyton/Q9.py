import re
w=input("Enter the word")
x="^[A-Z]\w{5,10}[A-Z]$"
matcher=re.fullmatch(x,w)
if matcher is not None:
    print("Valid")
else:
    print("not valid")