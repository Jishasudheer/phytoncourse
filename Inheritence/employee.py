class Person:
    def setvalues(self,name,age):
        self.name=name
        self.age=age
    def print(self):
        print(self.name," ",self.age)
class Parent:
    def set(self,name):
        self.name=name

class Employee(Person,Parent)