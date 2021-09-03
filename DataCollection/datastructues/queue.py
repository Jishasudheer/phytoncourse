q=[]
front=0
rear=0
size=5
def enqueue():
    global front,rear
    while rear<size:
        ele=int(input("Enter the elements"))
        q.insert(rear,ele)
        rear+=1
    if rear>=size:
        print("Que is full")
def dequeue():
    global front,rear
    if(front==rear):
        print("Queue is empty")
    else:
        q.pop(0)
        front+=1
def display():
    print(q)

while(True):
    print("1.enque 2.dequee  3.display  4.exit")
    ch=int(input("Enter choice"))
    if(ch==4):
        break
    while(ch<=3):
        if(ch==1):
            enqueue()
            break
        if ch==2:
            dequeue()
            break
        if ch==3:
            display()
            break
