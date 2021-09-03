import re
word=input("enter the word")
x= "^a[a-zA-Z0-9\W]*b$"
match=re.fullmatch(x,word)
if match is not None:
    print("valid")
else:
    print("Invalid")