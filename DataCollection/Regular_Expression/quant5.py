import re
x="a{1,3}"
r="jishaa 789 FAaaGHS YERaT"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())