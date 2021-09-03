class A:
    def printA(self):
        print("Inside A")
class B(A):
    def printB(self):
        print("Inside B")
class C(B):
    def printC(self):
        print("Inside C")
a=A()
a.printA()
print("\r")

b=B()
b.printB()
b.printA()
print("\r")

c=C()
c.printC()
c.printB()
c.printA()

