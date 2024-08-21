a,b=map(int,input().split())
grp=[[0,0]]
dp=[[0]*(b+1) for _ in range(a+1)]
for _ in range(1,a+1):
    x,y=map(int,input().split())
    grp.append([x,y])

for i in range(1,a+1):
    w=grp[i][0]
    v=grp[i][1]
    for j in range(1,b+1):
        if j<w:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-w]+v)
print(dp[a][b])