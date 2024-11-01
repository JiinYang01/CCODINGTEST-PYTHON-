from collections import deque
a=int(input())
grp=[0]*(a+1)
grp[0]=1
grp[1]=1
for i in range(2,a+1):
    for j in range(i,a):
        if i*j>a:
            break
        grp[i*j]=1
grrp=[]
for i in range(len(grp)):
    if grp[i]==0:
        grrp.append(i)
start=0
end=0
ans=0
g=deque([])
x=0


while start<len(grrp)-1 and end<=len(grrp)-1:
    if x<a:
        x+=grrp[end]
        g.append(grrp[end])
        if end<=len(grrp)-2:
            end+=1
    else:
        if x==a:
            ans+=1
        start+=1
        x-=g[0]
        g.popleft()

if a in grrp:
    ans+=1
print(ans)
    