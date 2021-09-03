class Person:
    def set(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print(self.name)
        print(self.age)
class Child:
    def setchild(self,name,age):
        self.name=name
        self.age=age
        print(self.name)
        print(self.age)
class Student(Person,Child):
    def print(self,roll,mark):
        self.rollno=roll
        self.mark=mark

s=Student()
s.setchild("jisha",35)
s.set("kiran",56)
s.print()


