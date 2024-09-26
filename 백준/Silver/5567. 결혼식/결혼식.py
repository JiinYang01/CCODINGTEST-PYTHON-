from collections import deque
a=int(input())
b=int(input())
grp=[[] for _ in range(a+1)]

for _ in range(b):
    x,y=map(int,input().split())
    grp[x].append(y)
    grp[y].append(x)

g=[[i,0] for i in range(a+1)]
visited=[False]*(a+1)

def BFS():
    q=deque([1])
    visited[1]=True
    while q:
        x1=q.popleft()
        for i in (grp[x1]):
            if not visited[i]:
                visited[i]=True
                g[i][1]=g[x1][1]+1
                q.append(i)
BFS()
ans=0
for i in g:
    if 0<i[1]<=2:
        ans+=1
print(ans)
