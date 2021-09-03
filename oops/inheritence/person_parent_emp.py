class Employee:
    def set_employee(self,id,name,salary,dept):
        self.id=id
        self.name=name
        self.salary=salary
        self.dept=dept
        print(self.id," ",self.name," ",self.salary," ",self.dept)
class Person(Employee):
    def setvalues(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
        print(self.name," ",self.age," ",self.address)
p1=Person()
p1.setvalues("jisha",35,"Mangalathu")
p1.set_employee(1102,"Jisha",15000,"Audit")