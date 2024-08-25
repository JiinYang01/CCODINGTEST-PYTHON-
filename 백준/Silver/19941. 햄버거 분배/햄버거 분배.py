from collections import deque
a,b=map(int,input().split())
grp=list(input())
cnt=0
visit=[0]*(a)
q=deque([])
for i in range(0,a):
    if grp[i]=='P':
        q.append(i)

while q:
    x=q.popleft()
    nx=x-b
    ny=x+b
    if nx<0:
        nx=0
    if a<=ny:
        ny=a-1
    for i in range(nx,ny+1):
            if grp[i]=='H' and visit[i]==0:
                visit[i]=1
                cnt+=1
                break
print(cnt)
