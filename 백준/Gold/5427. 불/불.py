from collections import deque
n=int(input())
ans=[]
for _ in range(n):
    qs=deque([])
    qf=deque([])
    x1,y1=map(int,input().split())
    grp=[]
    for _ in range(y1):
        k=list(input())
        grp.append(k)

    visits=[[0]*x1 for _ in range(y1)]
    visitf=[[0]*x1 for _ in range(y1)]

    for i in range(y1):
        for j in range(x1):
            if grp[i][j]=='*':
                visitf[i][j]=1
                qf.append((i,j))
            if grp[i][j]=='@':
                visits[i][j]=1
                qs.append((i,j))

    def BFSF():
        dx=[-1,1,0,0]
        dy=[0,0,-1,1]
        while qf:
            x,y=qf.popleft()
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<y1 and 0<=ny<x1:
                    if visitf[nx][ny]==0 and grp[nx][ny]!='#':
                        visitf[nx][ny]=visitf[x][y]+1
                        qf.append((nx,ny))
        return
    def BFSS():
        global ans
        dx=[-1,1,0,0]
        dy=[0,0,-1,1]
        while qs:
            x,y=qs.popleft()
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if nx<0 or ny<0 or y1<=nx or x1<=ny:
                    ans.append(visits[x][y])
                    return
                if 0<=nx<y1 and 0<=ny<x1:
                    if visits[nx][ny]==0 and grp[nx][ny]!='#':
                        if visits[x][y]+1<visitf[nx][ny] or visitf[nx][ny]==0:
                            qs.append((nx,ny))
                            visits[nx][ny]=visits[x][y]+1
        ans.append('IMPOSSIBLE')
        return
                            
    BFSF()
    BFSS()

for i in ans:
    print(i)
