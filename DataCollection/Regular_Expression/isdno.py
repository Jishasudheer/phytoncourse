import re
ph=input("enter the phone number")
x="[+][9][1]+[0-9]{10}$"
match=re.fullmatch(x,ph)
if match is not None:
    print("valid")
else:
    print("Invalid")