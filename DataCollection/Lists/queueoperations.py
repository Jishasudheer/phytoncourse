queue=[]
size=0
rear=0
front=0

def enqueue(queue, size):
    global rear
    while (rear <= size):
        element = int(input("Enter the element to be insert"))
        #queue.append(element)
        queue.insert(rear,element)# inserting the elment in the position rear
        rear += 1
        if (rear >= size):
            print("Queue is full")
            break

def dequeue(queue,size):
    global front,rear
    if(front==rear):
        print("Queue is empty")
    else:
        queue.pop(0)
        front=front+1

def display(queue,size):
    print(queue)

while True:
    print("1.Enqueue  2.Dequeue  3.display 4 Exit")
    choice=int(input("Enter your choice"))
    if choice ==4 :
        break
    if choice >=5 or choice<=0:
        print ("Invalid choice ")
        print("Enetr a valid choice")
    while(choice<=3 ):
        if(choice == 1 ):
            size=int(input("Enter the size of the queue"))
            enqueue(queue, size)
            break
        elif(choice == 2):
            dequeue(queue,size)
            break
        elif(choice == 3):
            display(queue,size)
            break