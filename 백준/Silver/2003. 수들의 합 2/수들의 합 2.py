a,b=map(int,input().split())
grp=list(map(int,input().split()))
s=0
e=0
an=0
ans=0
while s<a and s<=e:
    while an<b and e<a:
        an+=grp[e]
        e+=1
    if an==b:
        ans+=1
    if an>=b:
        an-=grp[s]
        s+=1
    if e>=a and an<b:
        break


print(ans)