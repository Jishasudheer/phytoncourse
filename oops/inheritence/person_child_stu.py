class Person:#Base class
    def setvalue(self,name,age):
        self.name=name
        self.age=age
        print(self.name," ",self.age)
class Child(Person):#Base class
    def setvalues(self,school,std):
        self.school=school
        self.std=std
        print(self.school," ",self.std)
class Student(Child):#derived class
    def set_student(self,rollno,mark):
        self.rollno=rollno
        self.mark=mark
        print(self.rollno," ",self.mark)
p=Person()
p.setvalue("jsiha",35)
print()
c=Child()
c.setvalues("SN ","5E")
c.setvalue("Sumi",10)
print()
s=Student()
s.set_student(110,450)
s.setvalues("SN","2A")
s.setvalue("Adya",7)