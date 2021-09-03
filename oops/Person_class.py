class Person:
    def setvalue(self,name,age):
        self.name=name #instance variable
        self.age=age
    def printvalue(self):
        print("Name=",self.name)
        print("Age=",self.age)

pe1=Person()
pe1.setvalue("Jisha",35)
pe1.printvalue()