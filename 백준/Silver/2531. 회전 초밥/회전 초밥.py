from collections import deque
a,b,c,d=map(int,input().split())
grp=[]
for i in range(a):
    s=int(input())
    grp.append(s)
grp.extend(grp)
start=0
end=0
ans=deque([])
an=0
ann=0
while end<a+c:   
    if end-start+1<=c:
        ans.append(grp[end])
        end+=1
    else:
        start+=1
        ans.popleft()
    if len(ans)==c:
        ans.append(d)
        an=max(an,len(set(ans)))
        ans.pop()
print(an)