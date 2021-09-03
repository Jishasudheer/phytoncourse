import re
word=input("enter the word")
x="[a-zA-Z]+\d$"
match=re.fullmatch(x,word)
if match is not None:
    print("valid")
else:
    print("Invalid")