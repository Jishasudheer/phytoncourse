import re
v_no=input("enter the vehicle number")
x="[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{4}$"
match=re.fullmatch(x,v_no)
if match is not None:
    print("valid")
else:
    print("Invalid")

