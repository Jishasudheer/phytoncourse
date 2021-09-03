def admin_required(func):
    def wrapper(a,b):
        if(a!="admin"):
            raise Exception("You are not allowed")
        else:
            return func(a,b)
    return wrapper
@admin_required
def change_pin(user,pin):
    mypin=pin
    return mypin

@admin_required
def account_delete(user,acc):
     return str(acc)+("delete")

print(change_pin("admin",1100))
print(account_delete("admin",1000))