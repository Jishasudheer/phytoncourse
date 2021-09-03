import re
x="^a"
r="avjishaa 789 FAaaGHS YERaT"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())