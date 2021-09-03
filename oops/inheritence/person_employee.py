class Person:
    def setvalues(self,name,age):
        self.name=name
        self.age=age
    def printvalues(self):
        print(self.name)
        print(self.age)
class Employee(Person):
    def setemployee(self,id,company):
        self.id=id
        self.company=company
    def printemployee(self):
        print(self.id)
        print(self.company)
emp=Employee()
emp.setvalues("jisha",35)
emp.setemployee(110,"X cloud")
emp.printvalues()
emp.printemployee()