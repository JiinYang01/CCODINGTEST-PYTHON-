a,b=map(int,input().split())
grp=[[]]
for i in range(a):
    x=list(map(int,input().split()))
    grp.append(x)
grp.sort()
dp=[[0]*(b+1) for _ in range(a+1)]

for i in range(1,a+1):
    w=grp[i][0]
    v=grp[i][1]
    for j in range(1,b+1):
        if w>j:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(v+dp[i-1][j-w],dp[i-1][j])

print(dp[a][b])