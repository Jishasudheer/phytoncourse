import re
word=input("Enter the word")
x="^[A-Z][a-z]+$"
match=re.fullmatch(x,word)
if match is not None:
    print("Valid")
else:
    print("Invalid")
