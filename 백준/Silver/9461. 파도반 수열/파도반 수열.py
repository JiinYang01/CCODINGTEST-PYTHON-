a=int(input())
grp=[]
for _ in range(a):
    a1=int(input())
    dp=[0]*(a1+1)
    if a1==1:
        grp.append(1)
    if a1==2:
        grp.append(1)
    if a1==3:
        grp.append(1)
    if a1>=4:
        dp[1]=1
        dp[2]=1
        dp[3]=1
        for i in range(4,a1+1):
            dp[i]=dp[i-2]+dp[i-3]
        grp.append(dp[a1])

for i in grp:
    print(i)
    