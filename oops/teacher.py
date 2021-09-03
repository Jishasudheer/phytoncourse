class Teacher:
    college_name="Tharanallur Arts and Science"
    def __init__(self,t_name,subject,t_id,dept):
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
name=input("Enter teacher name")
subject=input("Enter Subject")
id=input("Enter id")
dept=input("Enter Department")
t1=Teacher(name,subject,id,dept)
# t1=Teacher("Anu","Computer",1102,"computer")
t1.printdetails()
