#......single inheritence.....
class Person:   #Parent class/Base class/super class
    def walk(self):
        print("Person is walking")
    def read(self):
        print("Person is reading")
class Student(Person): #derived class/sub class/child class
    def exam(self):
        print("Student is attending exam....")
se=Student()
se.read()
se.walk()
se.exam()
