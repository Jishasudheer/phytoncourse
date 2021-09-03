from xmlrpc.client import SafeTransport


class Student:
    collegename="St.Thomas"
    def __init__(self,name,rollno,dept):
        self.name=name
        self.rollno=rollno
        self.dept=dept
    def printVal(self):
        print("Name         :",self.name)
        print("Roll no      :",self.rollno)
        print("Department   :",self.dept)
        print("College name :",Student.collegename)
    def __str__(self):
        return self.name+self.dept+str(self.rollno)
        # This method is used to reference an object attribute
        # converting integer into string
        # if we are not using this method we will get an memory address that point to the object
s=Student("Jisha",110,"computer")
s.printVal()
print("Reference is given as.......name+dept :",s)