a,b=map(int,input().split())
grp=[]
dp=[[0]*b for _ in range(a)]
for i in range(a):
    f=list(map(int,input().split()))
    grp.append(f)
dp[0][0]=grp[0][0]
for i in range(1,b):
    dp[0][i]=dp[0][i-1]+grp[0][i]

for j in range(1,a):
    dp[j][0]=dp[j-1][0]+grp[j][0]
for i in range(1,a):
    for j in range(1,b):
        dp[i][j]=max(dp[i-1][j]+grp[i][j],dp[i][j-1]+grp[i][j],dp[i-1][j-1]+grp[i][j])

print(dp[a-1][b-1])