# Create a Book class with instance Library_name, book_name, author, pages?
class Book:

    def __init__(self,library_name,b_name,author,pages):
        self.library_name=library_name
        self.b_name=b_name
        self.author=author
        self.pages=pages
    def printValues(self):
        print(self.library_name+"  "+self.b_name+" "+self.author+"  "+str(self.pages))
l=Book("College Library","Advanced python","Smith Arora",1000)
l.printValues()
