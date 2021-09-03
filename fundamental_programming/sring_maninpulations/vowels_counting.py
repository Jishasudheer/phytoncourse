
string=input("Enter a String")
count=0
vowel="aeiouAEIOU"
for i in string:
    if i in vowel:
        count=count+1
print("Number of voweals in the given string=",count)