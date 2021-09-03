import re
n=input("Enter a word")
# x='[a-z]+'
x="[\w]*"
match=re.fullmatch(x,n)
if match is not None:
    print("Valid")
else:
    print("not valid")