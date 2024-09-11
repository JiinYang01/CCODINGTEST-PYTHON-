from collections import deque
a=int(input())
grp=[[] for _ in range(a+1)]
while True:
    x,y=map(int,input().split())
    if x==-1 and y==-1:
        break
    grp[x].append(y)
    grp[y].append(x)

def bfs(start,visited,cnt):
    visited[start]=True
    q=deque([start])
    while q:
        s=q.popleft()
        for i in grp[s]:
            if not visited[i]:
                visited[i]=True
                cnt[i]=cnt[s]+1
                q.append(i)
    return

dp=[0]*(a+1)        
for i in range(1,a+1):
    visited=[False]*(a+1)
    cnt=[0]*(a+1)
    bfs(i,visited,cnt)
    dp[i]=max(cnt)

ans=min(dp[1:])
ans2=0
ans3=[]
aa=0

for i in dp[1:]:
    aa+=1
    if i==ans:
        ans2+=1
        ans3.append(aa)

print(ans,ans2)
print(*ans3)