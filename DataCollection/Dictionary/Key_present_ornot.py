# Searching a key in dictionary

dict= {'Name':'jisha','age':'35','Class':'First'}
key=input("Enter the Key ")

def search_dict (dict,key):

    if key in dict:
        print("Key Present")
    else:
        print("Key Not Present")


search_dict(dict,key)