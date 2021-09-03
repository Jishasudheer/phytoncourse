def fibonacci(num):
    if num <= 1 :
        return num
    else:
        return fibonacci(num-1)+fibonacci(num-2)

limit=int(input("Enter the limit"))
for i in range (limit):
    print(fibonacci(i))