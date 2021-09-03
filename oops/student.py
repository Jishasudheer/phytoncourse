class Student:
    def setvalues(self,rollno,name,cla,scho):
        self.rollno=rollno
        self.name=name
        self.cla=cla
        self.scho=scho
    def printvalues(self):
        print("Rollno : ",self.rollno)
        print("Name : ",self.name)
        print("Class : ",self.cla)
        print("School : ",self.scho)

s1=Student()
s1.setvalues(11,"Eshwar","5E","SN Vidhyabhavan")
s1.printvalues()

s2=Student()
print("\n")
s2.setvalues(22,"Adya","5E","SN Vidhyabhavan")
s2.printvalues()