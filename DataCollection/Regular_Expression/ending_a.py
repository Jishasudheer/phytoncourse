import re
x="a$"
r="jishaa 789 FAaaGHS YERaTaba"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())