from collections import deque
a,b=map(int,input().split())
grp=list(map(int,input().split()))
q=deque([ _ for _ in range(1,a+1)])

cnt=0
for i in grp:
        while True:
            if i==q[0]:
                q.popleft()
                break  
            else:
                if q.index(i)<((1+len(q))//2):
                    q.rotate(-1)
                    cnt+=1
                    continue
                else:
                    q.rotate(1)
                    cnt+=1
                    continue

print(cnt)
