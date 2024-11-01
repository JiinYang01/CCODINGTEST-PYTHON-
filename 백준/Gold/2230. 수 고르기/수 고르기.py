a,b=map(int,input().split())
grp=[]
for i in range(a):
    x=int(input())
    grp.append(x)
grp.sort()
start=0
end=0
ans=2000000000
tmp=0
while start<a and end<a:
    tmp=grp[end]-grp[start]
    if tmp==b:
        ans=tmp
        break
    if tmp>b:
        ans=min(ans,tmp)
        start+=1
    else:
        end+=1


print(ans)