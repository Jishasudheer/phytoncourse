class Person:#Base class
    def setperson(self,name,age,desig):
        self.name=name
        self.age=age
        self.desg=desig
        print(self.name," ",self.age,self.desg)
class Teacher(Person):
    college_name="Tharanallur Arts and Science"
    def setvalue(self,t_name,subject,t_id,dept):
        self.t_name=t_name
        self.subject=subject
        self.t_id=t_id
        self.dept=dept
        print("dept",self.dept)
    def printdetails(self):
        print("------------------printintg teacher details---------------")
        print("Teacher name :",self.t_name)
        print("Teacher id :",self.t_id)
        print("Subject :",self.subject)
        print("Department",self.dept)
        print("College Name :",Teacher.college_name)
        print("-----------------------------------------------------------")
t1=Teacher()
t1.setvalue("Jisha","comp",1120,"maths")
t1.printdetails()
t1.setperson("isha",35,"Teacher")