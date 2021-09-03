# class Wordcount:
#     def setvalues(self,count):
#         self.count=0
#         f1=open('content','r')
#         for i in f1:
#             self.count+=1
#     def printval(self):
#         print(self.count)
# w=Wordcount()
# w.setvalues(0)
# w.printval()
count={}
f=open("content","r")
for n in f:
    w=n.split(" ")
    for word in w:
        if word not in count:
            count.update({word:1})
        else:
            val=int(count[word])
            val+=1
            count.update({word:val})
print(count)
