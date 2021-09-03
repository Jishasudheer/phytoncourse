class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printvalues(self):
        print(self.name)
        print(self.age)
class Employee(Person):
    def __init__(self,id,company,name,age):
        super().__init__(name,age)
        self.id=id
        self.company=company
    def printemployee(self):
        print(self.id)
        print(self.company)
        print(self.name)
        print(self.age)
emp=Employee(1102,"X cloud","jisha",35)
emp.printemployee()
print()
emp.printvalues()