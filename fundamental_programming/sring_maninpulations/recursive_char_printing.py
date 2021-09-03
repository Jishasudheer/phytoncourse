str=input("Enter a String")
copystr=""
for i in str:
           if i not in copystr:

               copystr=copystr+i
           else:
               print("First recurive character is :: ",i)
               break





