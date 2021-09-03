# Two types of variables in class
#     static variable...related to class....access using classname
#     instance variable....related to methods....access using self keyword

class Student:
    scho='SN Vidhya Bhavan'
    def setvalues(self,rollno,name,cla):
        self.rollno=rollno
        self.name=name
        self.cla=cla

    def printvalues(self):
        print("Rollno : ",self.rollno)
        print("Name : ",self.name)
        print("Class : ",self.cla)
        print("School : ",Student.scho)

s1=Student()
s1.setvalues(11,"Eshwar","5E")
s1.printvalues()

s2=Student()
print("\n")
s2.setvalues(22,"Adya","2A")
s2.printvalues()