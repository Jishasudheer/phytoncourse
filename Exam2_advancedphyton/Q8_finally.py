#With error
lst=[8,5,6,9]
try:
    print(lst[6])
except:
    print("Error occured")
finally:
    print("printing finally block")

#without error
lst = [8, 5, 6, 9]
try:
    print(lst[2])
except:
    print("Error occured")
finally:
    print("printing finally block")
