def revert_val(func):
    def wrapper(n1,n2):
        if n1<n2:
            (n1,n2)=(n2,n1)
            return func(n1,n2)
        else:
            return func(n1,n2)
    return wrapper

@revert_val
def div(n1,n2):
    return n1/n2
print(div(2,10))

@revert_val
def sub(no1,no2):
    return no1-no2
print(sub(1,10))
