a=int(input())
grp=list(map(int,input().split()))
dp=[0]*a
dp[0]=grp[0]
for i in range(a):
    for j in range(i):
        if grp[i]>grp[j]:
            dp[i]=max(dp[i],dp[j]+grp[i])
        else:
            dp[i]=max(grp[i],dp[i])

print(max(dp))
