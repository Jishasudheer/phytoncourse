#---Multiple inheritence----
class Person:#Base class
    def setvalue(self,name,age):
        self.name=name
        self.age=age

        print(self.name," ",self.age)
class Child:#Base class
    def setvalues(self,school,std):
        self.school=school
        self.std=std
        print(self.school," ",self.std)
class Student(Person,Child):#derived class
    def set_student(self,rollno,mark):
        self.rollno=rollno
        self.mark=mark
        print(self.rollno," ",self.mark)
s=Student()
s.setvalue("Jisha",5)
s.setvalues("SN","5E")
s.set_student(10,450)


