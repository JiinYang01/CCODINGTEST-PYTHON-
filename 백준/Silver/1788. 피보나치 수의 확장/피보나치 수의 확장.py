p=int(input())
a=abs(p)
dp=[0]*(1000001)
dp[1]=1
if a>=2:
    dp[2]=1
if a>2:
    for i in range(3,a+1):
        dp[i]=(dp[i-2]+dp[i-1])%1000000000

if p==0:
    print(0)
elif p<0 and p%2==0:
    print(-1)
else:
    print(1)
print(dp[a])