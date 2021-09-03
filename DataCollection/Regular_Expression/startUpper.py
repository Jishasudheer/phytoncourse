import re
word=input("enter the word")
x= "^[A-Z][a-zA-Z0-9\W]$"
match=re.fullmatch(x,word)
if match is not None:
    print("valid")
else:
    print("Invalid")