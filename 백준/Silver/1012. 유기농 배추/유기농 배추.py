from collections import deque

def BFS(aa,bb,grp):
    queue=deque([(aa,bb)])
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    while queue:
        x1,y1=queue.popleft()
        for i in range(4):
            nx=x1+dx[i]
            ny=y1+dy[i]
            if 0<=nx<x and 0<=ny<y:
                if grp[nx][ny]==1:
                    grp[nx][ny]=0
                    queue.append((nx,ny))
    return 1

ans=[]
a=int(input())
for i in range(a):
    cnt=0
    x,y,z=map(int,input().split())
    grp=[[0]*y for _ in range(x)]
    for i in range(z):
        a1,b1=map(int,input().split())
        grp[a1][b1]=1
        
    for i in range(x):
            for j in range(y):
                    if grp[i][j]==1:
                        BFS(i,j,grp)
                        cnt+=1
    ans.append(cnt)
for i in ans:
    print(i)    

