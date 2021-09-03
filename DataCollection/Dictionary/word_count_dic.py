sen="jisha sudhi jisha sudhi jisha adya jisha eshwar"
word=sen.split(" ")
count={}
for i in word:
   if i not in count:
      count.update({i:1})
   else:
      val=int(count[i])
      val=val+1
      count.update({i:val})
print(count)