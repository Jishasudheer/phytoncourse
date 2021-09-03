str=input("Enter a String")
result=""
unwanted=":;,.{}[]*&^%$#@()"" "
for i in str:
    #if i.isalnum():
    if i not in unwanted:
        result=result+i
print(result)