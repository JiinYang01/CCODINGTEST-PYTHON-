import sys
input = sys.stdin.readline
a=int(input())
b=int(input())
grp=list(input())
ans=abs(a-100)

for i in range(1000001):
    i=str(i)
    cnt=0
    for j in range(len(i)):
        if i[j] in grp:
            break
        else:cnt+=1
    if cnt==len(i):
        ans=min(ans,len(i)+abs(int(i)-a))
        



print(ans)
    