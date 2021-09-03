import re
x='\d'
matcher=re.finditer(x,"jisha 789 FGHS YERT")
for match in matcher:
    print(match.start())
    print(match.group())