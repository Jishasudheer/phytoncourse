import re
x="a{2}"
r="aaajishaa 789 FAaaGHS YERaaT"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())