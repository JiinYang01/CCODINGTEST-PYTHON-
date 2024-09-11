a=int(input())
dp=[0]*(a+1)
dp[1]=1
if a>=2:
    dp[2]=2
if a>2:
    for i in range(3,a+1):
        dp[i]=(dp[i-2]+dp[i-1])%15746

print(dp[a])
