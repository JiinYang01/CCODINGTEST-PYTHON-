from collections import deque
a,b,c=map(int,input().split())
grp=[[0]*b for _ in range(a)]
for _ in range(c):
    x1,y1=map(int,input().split())
    grp[x1-1][y1-1]=1
ans=[]
def BFS(xx,yy):
    q=deque([(xx,yy)])
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    cnt=0
    while q:
        x,y=q.popleft()
        grp[x][y]=0
        cnt+=1
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<a and 0<=ny<b:
                if grp[nx][ny]!=0:
                    grp[nx][ny]=0
                    q.append((nx,ny))
    return cnt

for i in range(a):
    for j in range(b):
        if grp[i][j]==1:
            ans.append(BFS(i,j))
print(max(ans))