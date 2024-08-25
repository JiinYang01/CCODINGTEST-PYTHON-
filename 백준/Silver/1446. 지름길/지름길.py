a,b=map(int,input().split())
dp=[0]*(b+1)
grp=[]
for i in range(a):
    s=list(map(int,input().split()))
    grp.append(s)

for i in range(1,b+1):
    dp[i]=dp[i-1]+1
    for j in grp:
        if j[1]>b:
           continue
        if j[1]==i:
            dp[i]=min(dp[i],dp[j[0]]+j[2])

print(dp[-1])
