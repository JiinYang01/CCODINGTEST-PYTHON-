a,b=map(int,input().split())
x=list(map(int,input().split()))
start=1
end=max(x)
ans=0

while start<=end:
    mid=(start+end)//2
    cnt=0
    for i in (x):
        cnt+=(i//mid)
    if a<=cnt:
        ans=max(ans,mid)
        start=mid+1
    else:
        end=mid-1

print(ans)