def solution(m, n, puddles):
    answer = 0
    grp=[[0]*m for _ in range(n)]
    grp[0][0]=1
    if [1,2] not in puddles:
        grp[1][0]=1
    if [2,1] not in puddles:
        grp[0][1]=1

    for i in range(n):
        for j in range(m):
            if [j+1,i+1] not in puddles:
                if grp[i][j]==0 and i-1>=0 and j-1>=0:
                    grp[i][j]=grp[i-1][j]+grp[i][j-1]
                elif grp[i][j]==0 and i-1>=0 and j-1<0:
                    grp[i][j]=grp[i-1][j]
                elif grp[i][j]==0 and i-1<0 and j-1>=0:
                     grp[i][j]=grp[i][j-1]
        
    answer=grp[n-1][m-1]%1000000007
    return answer