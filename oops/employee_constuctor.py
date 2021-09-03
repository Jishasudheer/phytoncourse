class Employee:
    company="Xcloud"
    def __init__(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age
    def printvalue(self):
        print("Employee id =",self.id)
        print("Employee name=",self.name)
        print("Employee age=",self.age)
        print("Employee company=",Employee.company)

emp1=Employee(1102,"Jisha",35)
emp1.printvalue()
print("\n")
emp2=Employee(1123,"Hari",39)
emp2.printvalue()