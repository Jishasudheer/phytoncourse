import re
x="[^abc]"
matcher=re.finditer(x,"acj cjdefty$")
for match in matcher:
    print(match.start())
    print(match.group())
