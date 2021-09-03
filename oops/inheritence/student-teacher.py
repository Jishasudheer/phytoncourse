class Student:
    school="SN vidhyabhavan"
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def printval(self):
        print(self.name+"  "+self.rollno)
class Teacher(Student):
    def __init__(self,tname,subject,name,rollno):
        super().__init__(name,rollno)
        self.tname=tname
        self.subject=subject
    def printteacher(self):
        print(self.tname+" "+self.subject+" "+self.name)
    def __str__(self):
        return str(self.rollno)
t=Teacher("Jisha","Computer","Adya",1102)
t.printteacher()
print(t)




