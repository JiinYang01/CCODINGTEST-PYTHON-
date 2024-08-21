a=int(input())
d=[]
p=[]
dp=[0]*(a+1)
for i in range(a):
    x,y=map(int,input().split())
    d.append(x)
    p.append(y)

for i in range(a-1,-1,-1):
    if d[i]+i>a:
        dp[i]=dp[i+1]
    else:
        dp[i]=max(dp[i+1],dp[i+d[i]]+p[i])


print(max(dp))