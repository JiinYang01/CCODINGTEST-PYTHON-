from collections import deque
a,b=map(int,input().split())
grp=[]
visited=[[0]*b for _ in range(a)]
for i in range(a):
    k=input()
    grp.append(list(k))
ans_o=[]
ans_v=[]
def BFS(x,y):
    ocnt=0
    vcnt=0
    q=deque([(x,y)])
    if grp[x][y]=='.' or grp[x][y]=='v' or grp[x][y]=='o':
            visited[x][y]=1
            if  grp[x][y]=='v':
                        vcnt+=1
            if grp[x][y]=='o':
                        ocnt+=1
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    while q:
        x1,y1=q.popleft()
        for i in range(4):
            nx=x1+dx[i]
            ny=y1+dy[i]
            if 0<=nx<a and 0<=ny<b:
                if visited[nx][ny]!=1: 
                    if grp[nx][ny]=='.' or grp[nx][ny]=='v' or grp[nx][ny]=='o':
                        visited[nx][ny]=1
                        if  grp[nx][ny]=='v':
                            vcnt+=1
                        if  grp[nx][ny]=='o':
                            ocnt+=1
                        q.append((nx,ny))
    if vcnt>=ocnt:
         ans_v.append(vcnt)
    if ocnt>vcnt:
        ans_o.append(ocnt)
    return

for i in range(a):
    for j in range(b):
        if grp[i][j]!='#' and visited[i][j]!=1:
            BFS(i,j)

print(sum(ans_o),sum(ans_v))