import re
x="a*"
r="jisha 789 FAaGHS YERaT"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())