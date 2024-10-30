a,b=map(int,input().split())
x=list(map(int,input().split()))
start=0
end=0
ans=0
grp=[0]*(max(x)+1)

while start<a and end<a:
    if grp[x[end]]<b:
        grp[x[end]]+=1
        end+=1
    else:
        grp[x[start]]-=1
        start+=1
    ans=max(ans,end-start)
print(ans)