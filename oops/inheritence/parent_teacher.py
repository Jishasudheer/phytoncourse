class Parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printValues(self):
        print("name    :",self.name)
        print("age     :",self.age)
class Teacher(Parent):
    school="SN"
    def __init__(self,tname,id,sal,name,age):
        super().__init__(name,age)
        self.tname=tname
        self.id=id
        self.sal=sal
    def printTeacher(self):
        print("Teacher name :",self.tname)
        print("Teacher id   :",self.id)
        print("Salary      :",self.sal)
        print("School   :",Teacher.school)
        print("Parent name :",self.name)
        print("Parent age   :",self.age)
    def __str__(self):
        return(str(self.id))+self.tname
t1=Teacher("jisha",1102,30000,"Devan",28)
t1.printTeacher()
print(t1)