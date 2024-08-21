a=input()
ans=0
grp=a.split('-')
grp1=grp[0].split('+')
for i in grp1:
    ans+=int(i)

for i in grp[1:]:
    d=i.split('+')
    for j in d:
        ans-=int(j)    
print(ans)