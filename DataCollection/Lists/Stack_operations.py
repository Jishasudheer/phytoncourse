def stack_push(lst,size) :
    top=0
    while(top<=size):
            element=int(input("Enter the element to be insert"))
            lst.append(element)
            top+=1
            if(top>=size):
                print("Stack is full")
                break

def stack_pop(lst,size):
        if(size<=0):
            print("Empty stack")
            return
        else:
            lst.pop()
            size=size-1

def stack_display(lst,size):
    print (lst)

size=0
lst=[]
while True:
    print("1.Push  2.Pop  3.display 4 Exit")
    choice=int(input("Enter your choice"))
    if choice ==4 :
        break
    if choice >=5 or choice<=0:
        print ("Invalid choice ")
        print("Enetr a valid choice")
    while(choice<=3 ):
        if(choice == 1 ):
            size=int(input("Enter the size of the stack"))
            stack_push(lst, size)
            break
        elif(choice == 2):
            stack_pop(lst,size)
            size = size - 1
            break
        elif(choice == 3):
            stack_display(lst,size)
            break

        # elif(choice >=4 or choice<=0):
        #     print("Invalid Choice.")
        #     print()
        #     print("Enter a valid choice")
# stack_display(lst,size)
# stack_pop(lst,size)
# stack_display(lst,size)