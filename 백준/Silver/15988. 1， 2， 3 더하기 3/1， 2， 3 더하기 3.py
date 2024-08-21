import sys
a=int(sys.stdin.readline())
grp=[]

for _ in range(a):
    s=int(sys.stdin.readline())
    grp.append(s)

max_v=max(grp)
dp=[0]*(max_v+1)
dp[1]=1
dp[2]=2
dp[3]=4

if max_v>3:
    for i in range(4,max_v+1):
        dp[i]=(dp[i-2]+dp[i-1]+dp[i-3])%1000000009
for i in grp:
    print(dp[i])
   