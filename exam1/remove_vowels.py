str=input("Enter String")
count=0
for i in str:
    if i in 'a' or i in 'A' or i in 'e' or i in 'E' or i in 'I' or i in 'i' or i in 'o' or i in 'O':
        count+=1
print("No of Vowels=",count)