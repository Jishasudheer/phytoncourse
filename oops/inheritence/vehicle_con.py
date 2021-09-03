
class Vehicle:
    def __init__(self,model,reg,color):
        self.model=model
        self.reg=reg
        self.color=color
    def printValues(self):
        print("Model=",self.model)
        print("Register no=",self.reg)
        print("Color=",self.color)
    def __str__(self):
        return self.model+self.reg
v=Vehicle("Camery","KL84512","white")
v.printValues()
print(v)
