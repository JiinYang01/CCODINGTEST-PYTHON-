a,b=map(int,input().split())
grp=[list(map(int,input().split())) for _ in range(a)]
dp=[[0]*a for _ in range(a)]
dp[0][0]=grp[0][0]
for i in range(a):
    for j in range(a):
        if i<=0 and j<=0:
            continue
        if i<=0 and j>=1:
            dp[i][j]=dp[i][j-1]+grp[i][j]
        if i>=1 and j<=0:
            dp[i][j]=dp[i-1][j]+grp[i][j]
        if i>=1 and j>=1:
            dp[i][j]=dp[i-1][j]+dp[i][j-1]+grp[i][j]-dp[i-1][j-1]
ans1=[]
for _ in range(b):
    x,y,x1,y1=map(int,input().split())
    if 1<x and 1<y and 1<x1 and 1<y1:
        ans=(dp[x1-1][y1-1]-dp[x-2][y1-1]-dp[x1-1][y-2]+dp[x-2][y-2])
    if x<=1 and y<=1:
        ans=dp[x1-1][y1-1]
    if x>1 and y<=1:
        ans=dp[x1-1][y1-1]-dp[x-2][y1-1]
    if x<=1 and y>1:
        ans=dp[x1-1][y1-1]-dp[x1-1][y-2]
    ans1.append(ans)
    


for i in ans1:
    print(i)

