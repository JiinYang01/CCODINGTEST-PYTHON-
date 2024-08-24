
a,b=map(int,input().split())
grp=(list(map(int,input().split())))
grp.sort()

for i in range(b):
    x=grp[0]+grp[1]
    grp.remove(grp[0])
    grp.remove(grp[0])
    grp.append(x)
    grp.append(x)
    grp.sort()

print(sum(grp))