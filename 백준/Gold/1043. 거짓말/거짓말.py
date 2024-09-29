from collections import deque
a,b=map(int,input().split())
q=deque(list(map(int,input().split())))
q.popleft()
grp=[[] for _ in range(b)]

for i in range(b):
    f=list(map(int,input().split()))
    grp[i].extend(f[1:])

visited=[False]*(b)

visited1=[False]*(a+1)
for i in q:
    visited1[i]=True
while q:
    x=q.popleft()
    for i in range(b):
        if not visited[i]:
            if x in grp[i]:
                visited[i]=True
                for k in grp[i]:
                    if not visited1[k]:
                        visited1[k]=True
                        q.append(k)
print(visited.count(False))