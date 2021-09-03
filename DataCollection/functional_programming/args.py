#if we want to add more arguments we give it as *args.so we can add more arguments
# its return type is tuple

def dispaly(*args):
    return(args)
print(dispaly(1,3,5,6,4,9))