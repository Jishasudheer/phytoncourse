import re
word=input("enter the word")
x= "\D{8,15}$"
match=re.fullmatch(x,word)
if match is not None:
    print("valid")
else:
    print("Invalid")