from collections import deque

def bfs(grp,ans,n):
    q=deque([1])
    visited=[False]*(n+1)
    visited[1]=True
    while q:
        x=q.popleft()
        for i in grp[x]:
            if not visited[i]:
                visited[i]=True
                ans[i][1]=ans[x][1]+1
                q.append(i)
    return
                

def solution(n,edge):
    answer = 0
    ans=[[i,1] for i in range(n+1)]
    grp=[[] for _ in range(n+1)]
     
    for i in edge:
        grp[i[0]].append(i[1])
        grp[i[1]].append(i[0])
    bfs(grp,ans,n)
    a=sorted(ans,key=lambda ans:ans[1])
    
    for i in a:
        if i[1]==a[n][1]:
            answer+=1
    return answer