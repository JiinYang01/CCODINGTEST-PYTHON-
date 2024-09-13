x,y=map(int,input().split())
grp=list(map(int,input().split()))
ans=0
for i in range(1,len(grp)-1):
    s=max(grp[:i])
    s1=max(grp[i+1:len(grp)])
    a=min(s,s1)
    if grp[i]<a:
        ans+=(a-grp[i])
print(ans)