class Employee:
    company="Xcloud"
    def setvalue(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age
    def printvalue(self):
        print("Employee id =",self.id)
        print("Employee name=",self.name)
        print("Employee age=",self.age)
        print("Employee company=",Employee.company)

emp=Employee()
emp.setvalue(1102,"Jisha",35)
emp.printvalue()
print("\n")
emp.setvalue(1123,"Hari",39)
emp.printvalue()