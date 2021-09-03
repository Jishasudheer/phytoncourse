#construtor is used to initialize instance variable

class Person:
    def __init__(self,name,age,address):#constructor
        self.name=name
        self.age=age
        self.address=address
    def printvalues(self):
        print(self.name,"   ",self.age,"  ",self.address)
per=Person("Jisha",35,"Mangalathu")
per.printvalues()