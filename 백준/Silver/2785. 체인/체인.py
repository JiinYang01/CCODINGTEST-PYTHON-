from collections import deque
a=int(input())
grp=list(map(int,input().split()))
ans=0
grp.sort()
grp=deque(grp)
while True:
    if grp!=([]):
        x=grp.popleft()
    j=len(grp)-1
    if j-x==0:
        ans+=x
        break
    if j>x:
        for i in range(x):
            grp.pop()
        ans+=x
        continue
    if j<x:
        ans+=j+1
        break

print(ans)