class Addition:
    def setvalues(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def printsum(self):
        print("Sum=",self.n1+self.n2)
add=Addition()
add.setvalues(45,56)
add.printsum()
add.setvalues(40,52)
add.printsum()
