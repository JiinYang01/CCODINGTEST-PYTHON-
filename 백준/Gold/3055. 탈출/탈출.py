from collections import deque
a,b=map(int,input().split())
grp=[list(input())for _ in range(a)]

k_visited=[[0 for _ in range(b)] for _ in range(a)]
w_visited=[[0 for _ in range(b)] for _ in range(a)]

k_q=deque([])
w_q=deque([])

for i in range(a):
    for j in range(b):
        if grp[i][j]=='S':
            k_visited[i][j]=1
            k_q.append((i,j))
        if grp[i][j]=='*':
            w_visited[i][j]=1
            w_q.append((i,j))

def W_BFS():
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    while w_q:
        x,y=w_q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<a and 0<=ny<b:
                if w_visited[nx][ny]==0 and grp[nx][ny]!='X' and grp[nx][ny]!='D':
                    w_visited[nx][ny]=w_visited[x][y]+1
                    w_q.append((nx,ny))
    return

def K_BFS():
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    while k_q:
        x,y=k_q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<a and 0<=ny<b:
                if k_visited[nx][ny]==0 and grp[nx][ny] != 'X': 
                    if w_visited[nx][ny]==0:
                        k_visited[nx][ny]=k_visited[x][y]+1
                        k_q.append((nx,ny))
                    else:
                        if k_visited[x][y]+1<w_visited[nx][ny]:
                             k_visited[nx][ny]=k_visited[x][y]+1
                             k_q.append((nx,ny))
                

    return

W_BFS()
K_BFS()

for i in range(a):
    for j in range(b):
        if grp[i][j]=='D':
            if k_visited[i][j]!=0:
                print(k_visited[i][j]-1)
            else:
                print('KAKTUS')