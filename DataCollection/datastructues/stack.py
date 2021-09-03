size=5
top=0
sta=[]
def push():
    global top
    while(top<size):
            ele=int(input("Enter the elements"))
            sta.insert(top,ele)
            top+=1
            if top >= 5:
                print("Stack is full")
                break

def pop():
    global top
    if(top==0):
        print("Stack is empty")
    else:
        sta.pop()
        top-=1

def display():
    print(sta)

while(True):
    print("1.push   2.pop   3.display    4.exit")
    ch=int(input("Enter choice"))
    if (ch == 4):
        break
    while(ch<=3):
        if(ch==1):
            push()
            break
        if(ch==2):
            pop()
            break
        if(ch==3):
            display()
            break

