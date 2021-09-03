class Person:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def __str__(self):
        return (self.name)
p=Person("Jisha",1102)
print(p)