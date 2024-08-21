x=input()
a=[]
for i in x:
   a.append(int(i))
a.sort(reverse=True)
p=''
for i in a:
    p+=str(i)
print(p)