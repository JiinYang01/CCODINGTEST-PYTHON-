import sys
a=int(input())
grp=list(map(int,input().split()))
b=int(input())
grp.sort()
min1=1
max1=max(grp)
mid=(min1+max1)//2
if sum(grp)<=b:
    ans=(max(grp))
else:
    while min1<mid:
        cnt=0
        for i in grp:
            if i<mid:
                cnt+=i
            else:
                cnt+=mid
        if cnt>b:
            max1=mid
            mid=(min1+max1)//2
            continue
        if cnt<b:
            min1=mid
            mid=(min1+max1)//2
            continue
        if cnt==b:
            break
    ans=mid
print(ans)