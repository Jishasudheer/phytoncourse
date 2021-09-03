class Vehicle:
    def __init__(self,type,company):
        self.type=type
        self.company=company
    def display_Vehicle_details(self):
        print("Type     :",self.type)
        print("Company  :",self.company)
class Bus(Vehicle):
    def __init__(self,bname,bcolor,bmodel,type,company):
        super().__init__(type,company)
        self.bname=bname
        self.bcolor=bcolor
        self.bmodel=bmodel
    def print_Bus_details(self):
        print("Bus type     :",self.bname)
        print("Bus Color    :",self.bcolor)
        print("Bus Model    :",self.bmodel)

b=Bus("Mangalathu","Green and White","New Model","Bus","Yaris")
b.display_Vehicle_details()
b.print_Bus_details()
