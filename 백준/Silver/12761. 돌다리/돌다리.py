import sys
from collections import deque
n,m,x,y=map(int,input().split())
visited=[0]*100001

visited[x]=1

q=deque([x])

def bfs():
    while q:
        a=q.popleft()
        if a==y:
            print(visited[a]-1)
            sys.exit(0)
        k1,k2,na,na1,na2,nb,nb1,nb2=a+1,a-1,a+n,a-n,a*n,a+m,a-m,a*m
        if 0<=k1<len(visited):
            if visited[k1]==0:
                visited[k1]=visited[a]+1
                q.append(k1)
        if 0<=k2<len(visited):
            if visited[k2]==0:
                visited[k2]=visited[a]+1
                q.append(k2)
        if 0<=na<len(visited):
            if visited[na]==0:
                visited[na]=visited[a]+1
                q.append(na)
        if 0<=na1<len(visited):
            if visited[na1]==0:
                visited[na1]=visited[a]+1
                q.append(na1)
        if 0<=na2<len(visited):
            if visited[na2]==0:
                visited[na2]=visited[a]+1
                q.append(na2)
        if 0<=nb<len(visited):
            if visited[nb]==0:
                visited[nb]=visited[a]+1
                q.append(nb)
        if 0<=nb1<len(visited):
            if visited[nb1]==0:
                visited[nb1]=visited[a]+1
                q.append(nb1)
        if 0<=nb2<len(visited):
            if visited[nb2]==0:
                visited[nb2]=visited[a]+1
                q.append(nb2)
    return

bfs()


