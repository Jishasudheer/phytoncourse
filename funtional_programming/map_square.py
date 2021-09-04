# map ->map(function,list)
lst=[4,2,3,5]
def square(a):
    return(a**2)
print (list(map(square,lst)))

square=list(map(lambda a:a**2,lst))
print(square)