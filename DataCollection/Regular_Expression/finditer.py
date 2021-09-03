import re
count=0
matcher=re.finditer("ab","ababaaabbbab")
for match in matcher:
    print("match available at ...",match.start())#show match starting position
    print("group",match.group())#shows which group matches the string
    count+=1
print("Count=",count)

