a=int(input())
grp=[1]*10
dp=[1]*10
for k in range(a):
    grp[:]=dp[:]
    for i in range(1,10):
        dp[i]=dp[i-1]+grp[i]
print(dp[9]%10007)