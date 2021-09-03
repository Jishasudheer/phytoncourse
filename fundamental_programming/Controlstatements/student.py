name=input("Enter student name")
mark=int(input("Enter the mark"))
if mark>=90:
    print("A+")
elif 80<=mark<90:
    print("A")
elif 70<=mark<80 :
    print("B+")
elif 60<=mark<70 :
    print("B+")
elif 50<=mark<60 :
    print("C+")
elif 40<=mark<50 :
    print("C")
else:
    print("D")