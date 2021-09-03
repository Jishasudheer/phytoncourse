import re
word=input("enter the word")
x= "^a[0-9]*b$"
match=re.fullmatch(x,word)
if match is not None:
    print("valid")
else:
    print("Invalid")