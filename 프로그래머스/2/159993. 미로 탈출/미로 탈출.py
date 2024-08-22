from collections import deque
def solution(maps):
    answer = 0
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    q=deque([])
    grp=[[0]*len(maps[0]) for _ in range(len(maps))]
    visited=[[0]*len(maps[0]) for _ in range(len(maps))]
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j]=='S':
                q.append((i,j))
                grp[i][j]=1
                visited[i][j]=1
            if maps[i][j]=='L':
                xx,yy=i,j
                grp[i][j]=1
            if maps[i][j]=='E':
                grp[i][j]=1
                e1,e2=i,j
            if maps[i][j]=='O':
                grp[i][j]=1
    def  bfs_l():        
        while q:
            x,y=q.popleft()
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<len(maps) and 0<=ny<len(maps[0]):
                    if visited[nx][ny]!=1 and grp[nx][ny]!=0:
                        visited[nx][ny]=1
                        grp[nx][ny]=grp[x][y]+1
                        q.append((nx,ny))
                        if nx==xx and ny==yy:
                                    return
    visited1=[[0]*len(maps[0]) for _ in range(len(maps))]
    
    def  bfs_e():
        q1=deque([(xx,yy)])
        visited1[xx][yy]=1
        while q1:
            x,y=q1.popleft()
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<len(maps) and 0<=ny<len(maps[0]):
                    if visited1[nx][ny]!=1 and grp[nx][ny]!=0:
                        visited1[nx][ny]=1
                        grp[nx][ny]=grp[x][y]+1
                        q1.append((nx,ny))
                        if nx==e1 and ny==e2:
                                    return
    
    bfs_l()
    if visited[xx][yy]==1:
        bfs_e()

    if visited1[e1][e2]==0:
        answer=-1
    else:
        answer=grp[e1][e2]-1
    return answer

maps=["SOOOL", "OXXXX", "OXXXX", "OXXXX", "EXXXX"]
print(solution(maps))