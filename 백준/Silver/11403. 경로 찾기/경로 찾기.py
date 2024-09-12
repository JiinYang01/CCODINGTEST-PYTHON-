from collections import deque

a=int(input())
d=[]
grp=[[] for _ in range(a)]
for i in range(a):
    s=list(map(int,input().split()))
    d.append(s)

for i in range(a):
    for j in range(a):
        if d[i][j]==1:
            grp[i].append(j)


ans=[[0]*a for _ in range(a)]
def BFS(start):
    q=deque([start])
    visited=[False]*(a)
    while q:
        f=q.popleft()
        for i in grp[f]:
            if not visited[i]:
                visited[i]=True
                ans[start][i]=1
                q.append(i)
for i in range(a):
    BFS(i)
for i in ans:
    print(*i)

