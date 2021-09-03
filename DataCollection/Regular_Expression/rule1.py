import re
# x='[abc]' check wheter a or b or c is present if yes print its position
x="[^abc]"
matcher=re.finditer(x,"acj cjdefty$")
for match in matcher:
    print(match.start())
    print(match.group())
