import re
x='[a-zA-Z0-9]'
matcher=re.finditer(x,"jisha 789 FGHS YERT")
for match in matcher:
    print(match.start())
    print(match.group())