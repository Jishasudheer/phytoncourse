class Teacher:
    def __init__(self,name,age,sal):
        self.name=name
        self.age=age
        self.sal=sal
    def display(self):
        print(self.name)
        print(self.age)
        print(self.sal)
    def __str__(self):
        return self.name
t=Teacher("jisha",36,30000)
t.display()
print("ref ",t)
