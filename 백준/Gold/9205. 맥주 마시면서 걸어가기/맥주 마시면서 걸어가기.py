from collections import deque

d=int(input())
ans=[]
def bfs():
    queue=deque()
    queue.append((x,y))
    while queue:
        n1,n2=queue.popleft()
        if abs(n1-x2)+abs(n2-y2)<=1000:
            ans.append("happy")
            return
        for i in range(a):
            if visited[i]==0:
                nx,ny=graph[i]
                if abs(nx-n1)+abs(ny-n2)<=1000:
                    visited[i]=1
                    queue.append((nx,ny))
    ans.append("sad")
    return

for i in range(d):
    a=int(input())
    x,y=map(int,input().split())
    graph=[]
    for i in range(a):
        a1,b1=map(int,input().split())
        graph.append((a1,b1))

    x2,y2=map(int,input().split())
    visited=[0]*(a+1)
    bfs()
for i in ans:
    print(i)