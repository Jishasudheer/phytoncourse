# import re
# x="[a-zA-Z0-9\W]*[$a]"
# word=input("Enter word")
# match=re.fullmatch(x,word)
# if match is not None:
#     print("Valid exp")
# else:
#     print("Invalid")

# import re
# count=0
# x="ab"
# word=input("Enter the word")
# matcher=re.finditer(x,word)
# for match in matcher :
#     # match.start()
#     # match.group()
#     count+=1
# print(count)

# import re
# ph=input("Enter phone number")
# x="[\d]{10}$"
# match=re.fullmatch(x,ph)
# if match != None:
#     print("Valid")
# else:
#     print("Not valid")

# import re
# x="[a-zA-Z]+[0-9]?$"
# word=input("Enter word")
# match=re.fullmatch(x,word)
# if match is not None:
#     print("Valid")
# else:
#     print("Not valid")

# mail validation
# import re
# mail=input("Enter the mail id")
# rule="[a-zA-Z0-9_]+[@][a-z]+[.][a-z]{2,3}$"
# match=re.fullmatch(rule,mail)
# print(match)
# if match is not None:
#     print("Valid mail")
# else:
#     print("Not a valid mail id")
#

# import re
# word=input("Enter the word")
# rule="^a+[\w]*b$"
# match=re.fullmatch(rule,word)
# if match is not None:
#     print("Valid")
# else:
#     print
import re
word=input("Enter the word")
rule="^[A-Z]+[\w]*\W*$"
match=re.fullmatch(rule,word)
if match is not None:
    print("Valid")
else:
    print("Not valid")