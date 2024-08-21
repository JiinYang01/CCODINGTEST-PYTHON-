from collections import deque
f,s,g,u,d=map(int,input().split())
cnt=[0]*(f+1)
cnt[s]=1
def DFS():
    q=deque([s])
    while q:
        a=q.popleft()
        if a==g:
            print(cnt[a]-1)
            exit()
        ns=a+u
        if 1<=ns<=f and cnt[ns]==0:
            cnt[ns]=cnt[a]+1
            q.append(ns)
        nd=a-d
        if 1<=nd<=f and cnt[nd]==0:
            cnt[nd]=cnt[a]+1
            q.append(nd)
    print("use the stairs")
DFS()
