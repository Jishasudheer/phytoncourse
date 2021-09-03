class Vscode:
    def compile(self):
        print("Compiling using VScode")
    def execute(self):
        print("Excecute usng VScode")
    def debug(self):
        print("Debug using VScode")
class Pycharm:
    def compile(self):
        print("Compiling using Phycharm")
    def execute(self):
        print("Execute usingphycahrm")
    def debug(self):
        print("Debug using pycharm")
class Programmer:
    def coding(self,ide):
        ide.compile()
        ide.execute()
        ide.debug()
dev=Programmer()
pyc=Pycharm()
dev.coding(pyc)
vscode=Vscode()
dev.coding(vscode)