a=int(input())
grp=[]

for _ in range(a):
    x=list(map(int,input().split()))
    grp.append(x)

grp.sort()
start=grp[0][0]
end=grp[0][1]
ans=[]

for i in grp:
    if i[0]<end:
        if i[1]>end:
            end=i[1]
        if i[1]<start:
            start=i[1]
        continue   
    ans.append((start,end))   
    start=i[0]    
    end=i[1]
ans.append((start,end))
s=0
for i in ans:
    s+=i[1]-i[0]
print(s)