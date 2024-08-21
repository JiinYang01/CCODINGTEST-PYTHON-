from collections import deque
a,b,c=map(int,input().split())
grp=[[1]*b for _ in range(a)]
for _ in range(c):
    x1,y1,x2,y2=map(int,input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            grp[i][j]=0

cnt=0
ans=[]
def bfs(i,j):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    q=deque([(i,j)])
    grp[i][j]=0
    cnt=0
    while q:
        cnt+=1
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<a and 0<=ny<b:
                if grp[nx][ny]==1:
                    grp[nx][ny]=0
                    q.append((nx,ny))
    ans.append(cnt)

ans=[]
for i in range(a):
    for j in range(b):
        if grp[i][j]==1:
            bfs(i,j)
            cnt+=1
ans.sort()
print(cnt)
print(*ans)
            