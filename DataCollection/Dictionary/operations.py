dict = {'Name':'jisha','age':'35','Class':'First'}#Defining dictionary format

print(dict)
print(type(dict))

dict['age']=34 #update existing Entry
dict['School']='SN vidhya Bhavan' # adding new key
dict.update({'Location':'Thrissur'})#Another method to add new key
# print(dict['Name'])
# print("dict[Name] :",dict['Name'])
# print("dict[Age] :",dict['age'])
del dict['Name'] # deleting specified key
dict.clear() # Clearing all elements in dict
print(dict)
del dict # Deleting dictionary
print(dict)