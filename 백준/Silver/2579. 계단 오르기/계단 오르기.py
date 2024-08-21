a=int(input())
grp=[int(input())for _ in range(a)]
dp=[0]*303
dp[0]=grp[0]
if a>1:
    dp[1]=grp[0]+grp[1]
if a>2:
    dp[2]=max(grp[1]+grp[2],grp[0]+grp[2])
if a>3:
    for i in range(3,a):
        dp[i]=max(dp[i-2]+grp[i],dp[i-3]+grp[i-1]+grp[i])
print(dp[a-1])