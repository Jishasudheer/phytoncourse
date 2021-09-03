def age_check(func):
    def wrapper(name,age,place):
        if(age<18):
            raise Exception("Not eligible")
        else:
            return func(name,age,place)
    return wrapper
@age_check
def vaccine(name,age,place):
    return "eligible"

print(vaccine("Jisha",6,"Kaipamangalm"))



