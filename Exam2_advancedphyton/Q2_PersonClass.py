class Person:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
    def print_person_details(self):
        print("Person details.........")
        print(self.name+"  "+str(self.age)+"  "+self.address)
class Student(Person):
    collegename="Vijayagiri"
    def __init__(self,rollno,name,age,address):
        self.name=name
        self.rollno=rollno
        self.age=age
        self.address=address
    def print_student_details(self):
        print("Prtinting student details.......")
        print(str(self.rollno)+"  "+self.name+"  "+str(self.age)+"  "+self.address)

class Teacher(Student,Person):
    def __init__(self,subject,name,age,address):
        self.name=name
        self.age=age
        self.address=address
        self.subject=subject
    def print_Teacher_details(self):
        print("Teaher name:",self.name)
        print("subject    :",self.subject)
        print("College    :",Student.collegename)

te=Teacher("computer","Jisha",36,"Kaipamangalam Trissur")
te.print_Teacher_details()
p=Person("Hari",40,"Kottayam")
p.print_person_details()
s=Student(1102,"Adya",15,"Thrissur")
s.print_student_details()
