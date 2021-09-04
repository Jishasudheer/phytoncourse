lst=[2,3,5,4]
def cube(a):
    return(a**3)
print(list(map(cube,lst)))

cube=list(map(lambda num:num**3,lst))
print(cube)