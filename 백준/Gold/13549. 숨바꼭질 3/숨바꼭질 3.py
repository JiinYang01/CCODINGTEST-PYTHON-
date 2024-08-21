from collections import deque
a,b=map(int,input().split())
q=deque([a])
max1=100001
grp=[0]*(max1)

visited=[False]*(max1)
visited[a]=True
def bfs():
    while q:
        x=q.popleft()
        if x==b:
            break
        nx=x+1
        ns=x-1
        nq=x*2
        if 0<=nx<max1:
            if visited[nx]==False or grp[nx]>grp[x]+1:
                grp[nx]=grp[x]+1
                visited[nx]=True
                q.append(nx)
        if 0<=ns<max1:
            if visited[ns]==False or grp[ns]>grp[x]+1:
                grp[ns]=grp[x]+1
                visited[ns]=True
                q.append(ns)
        if 0<=nq<max1:
            if visited[nq]==False or grp[nq]>grp[x]:
                grp[nq]=grp[x]
                visited[nq]=True
                q.append(nq)
    return
bfs()
print(grp[b])
