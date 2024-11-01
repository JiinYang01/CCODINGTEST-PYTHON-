from collections import deque
a,b=map(int,input().split())
x=list(map(int,input().split()))
grp=[]
for i in x:
    if i%2==0:
      grp.append(0)
    else:
        grp.append(1)
ls=deque([])          
ans=0
start=0
end=0
tmp=0
ans1=0
while start<a and end<a:
    if tmp<=b:
        if grp[end]==0:
            ans1+=1
            ls.append(grp[end])
        else:
            tmp+=1
            ls.append(grp[end])
        end+=1
        ans=max(ans,ans1)
    else:
        start+=1
        tmp-=ls[0]
        if ls[0]==0:
            ans1-=1
        ls.popleft()

print(ans)