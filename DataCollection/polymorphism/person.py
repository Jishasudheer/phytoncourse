#overloading  .....same method name different number of arguments
#overriding....same method name same number of arguments
class Person:
    def show(self,num1):
        self.num1=num1
        print(self.num1)
class Student:
    def show(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print(self.num1,self.num2)
per=Person()
per.show(10)