from collections import deque
x=int(input())
grp=[]
rgb=[[0]*x for _ in range(x)]
grp_visited=[[0]*x for _ in range(x)]
rgb_visited=[[0]*x for _ in range(x)]
for i in range(x):
    a=input()
    grp.append(list(a))
for i in range(x):
    for j in range(x):
        if grp[i][j]=='R' or grp[i][j]=='G':
            rgb[i][j]+=1

def bfs(i,j,visited,grpp,c):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    q=deque([(i,j)])
    while q:
        x1,y1=q.popleft()
        for i in range(4):
            nx=x1+dx[i]
            ny=y1+dy[i]
            if 0<=nx<x and 0<=ny<x:
                if visited[nx][ny]==0 and grpp[nx][ny]==c:
                    visited[nx][ny]=1
                    q.append((nx,ny))
    return
ans=[]

cnt=0
for i in range(x):
    for j in range(x):
        if grp[i][j]=='R' and grp_visited[i][j]==0:
            cnt+=1
            bfs(i,j,grp_visited,grp,'R')
        if grp[i][j]=='G' and grp_visited[i][j]==0:
            cnt+=1
            bfs(i,j,grp_visited,grp,'G')
        if grp[i][j]=='B' and grp_visited[i][j]==0:
            cnt+=1
            bfs(i,j,grp_visited,grp,'B')
ans.append(cnt)

cnt=0
for i in range(x):
    for j in range(x):
        if rgb[i][j]==1 and rgb_visited[i][j]==0:
            cnt+=1
            bfs(i,j,rgb_visited,rgb,1)
        if rgb[i][j]==0 and rgb_visited[i][j]==0:
            cnt+=1
            bfs(i,j,rgb_visited,rgb,0)
ans.append(cnt)

print(*ans)

