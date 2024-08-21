x=(input())
p=[]
q=[]
for i in x:
    p.append(i)
for a,b in enumerate(p):
    if a==len(x)-1:
        q.append(b)
        break
    elif b!=x[a+1]:
        q.append(b)
        q.append(",")
    else:
        q.append(b)
x=q.count(',')
if x==1:
    print(x)
else:
    if x%2==0:
        print(x//2)
    else:
        print(x//2+1)