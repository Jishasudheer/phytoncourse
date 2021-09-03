class Person:#Base class
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print(self.name)
        print(self.age)
class Student(Person):#Base class
    def __init__(self,rollno,name,age):
        super().__init__(name,age)
        self.rollno=rollno
    def print(self):
        print(self.rollno)
cr=Student(10,"jisha",25)
cr.printval()
#cr.print()
