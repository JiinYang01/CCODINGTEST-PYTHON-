a=int(input())
grp=[]
dp=[0]*(a)

for i in range(a):
    x=int(input())
    grp.append(x)

dp[0]=grp[0]
if a>1:
    dp[1]=grp[1]+grp[0]
if a>2:
    dp[2]=max(grp[0]+grp[2],grp[1]+grp[2],dp[1])
if a>3:
    dp[3]=max(grp[0]+grp[2]+grp[3],grp[0]+grp[1]+grp[3],grp[1]+grp[2])
if a>4:
    for i in range(4,a):
            dp[i]=max(dp[i-4]+grp[i-2]+grp[i-1],dp[i-3]+grp[i-1]+grp[i],dp[i-2]+grp[i],dp[i-3]+grp[i-1])

print(dp[a-1])