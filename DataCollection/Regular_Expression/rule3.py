import re
x="[a-z]"#consider all lower case letters
matcher=re.finditer(x,"acj cjdefty$")
for match in matcher:
    print(match.start())
    print(match.group())
