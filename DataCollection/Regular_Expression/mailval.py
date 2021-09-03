import re
word=input("enter the mail")
x= '[a-zA-Z0-9]+[@][a-z]+[.][a-z]{2,3}$'
match=re.fullmatch(x,word)
if match is not None:
    print("valid")
else:
    print("Invalid")