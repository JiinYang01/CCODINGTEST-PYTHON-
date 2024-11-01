a,b=map(int,input().split())
grp=[]
for i in range(a):
    x=int(input())
    grp.append(x)

start=1
end=max(grp)
ans=0
tmp=0
k=0
while start<end:
    mid=int((start+end)//2)+1
    k=0
    for i in grp:
        k+=int(i//mid)
    if k>=b:
        tmp=mid
        start=mid+1
        ans=max(ans,tmp)
    else:
        end=mid-1
if b==1:
    ans=max(grp)
else:
    k=0
    for i in grp:
        k+=int(i//(ans+1))
        if k>=b:
            ans=ans+1
print(ans)
