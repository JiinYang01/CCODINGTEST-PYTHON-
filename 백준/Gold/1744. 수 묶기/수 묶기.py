a=int(input())
p=[]
m=[]
z=[]
o=[]
ans=[]
for _ in range(a):
    d=int(input())
    if d<0:
        m.append(d)
    if d==0:
        z.append(d)
    if d>1:
        p.append(d)
    if d==1:
        o.append(1)
p.sort(reverse=True)
q=0
m.sort()

if len(p)>=2:
    if len(p)%2==0:
        for i in range(0,len(p),2):
            q+=(p[i]*p[i+1])  
    else:
        for i in range(0,len(p)-1,2):
            q+=(p[i]*p[i+1]) 
        q+=p[len(p)-1]
if len(p)==1:
    q+=p[0]
if o!=[]:
    for i in o:
        q+=i

if len(m)==1 and z==[]:
    q+=m[0]
    m.pop()
if len(m)==1 and z!=[]:
    m.pop()
if m!=[]:
    if len(m)%2==0:
        for i in range(0,len(m),2):
            q+=(m[i]*m[i+1])
    else:
        for i in range(0,len(m)-1,2):
                a1=(m[i]*m[i+1])
                q=q+a1
        if z==[]:
                q+=m[len(m)-1]



print(q)