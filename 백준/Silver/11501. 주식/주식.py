#그리디알고리즘 백준 주식
k=int(input())
ans1=[]
for _ in range(k):
    d=int(input())
    grp=list(map(int,input().split()))
    end=len(grp)-1
    ans=0
    start=end-1
    max1=grp[end]  
    for j in grp[end::-1]:
        if j<=max1:
            ans+=max1-j         
        else:
            max1=j
    ans1.append(ans)
for i in ans1:
    print(i)