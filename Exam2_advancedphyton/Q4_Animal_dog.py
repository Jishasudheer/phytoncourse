class Animal:
    def __init__(self,name,type):
        self.name=name
        self.type=type
    def print_animal_details(self):
        print(self.name+"  "+self.type)
class Dog(Animal):
    def __init__(self,dname,size,name,type):
        super().__init__(name,type)
        self.dname=dname
        self.size=size
    def print_dog_details(self):
        print("Printing dog details")
        print(self.name+"  "+self.type+" "+self.dname+"  "+self.size)

d=Dog("Tintu","Small","Dog","Pomeran")
d.print_dog_details()