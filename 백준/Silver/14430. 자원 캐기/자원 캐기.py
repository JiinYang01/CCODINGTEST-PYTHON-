#백준 자원캐기

a,b=map(int,input().split())
grp=[list(map(int,input().split())) for _ in range(a)]
dp=[[0]*b for _ in range(a)]
ans=0
for i in range(a):
    for j in range(b):
        if 1<=i and 1<=j:
            grp[i][j]=max(grp[i-1][j]+grp[i][j],grp[i][j-1]+grp[i][j])
        if i<1 and j<1:
            grp[i][j]=grp[0][0]
        if i<1 and 1<=j:
            grp[i][j]=grp[i][j-1]+grp[i][j]
        if 1<=i and j<1:
            grp[i][j]=grp[i-1][j]+grp[i][j]
        ans=max(grp[i][j],ans)
print(ans)