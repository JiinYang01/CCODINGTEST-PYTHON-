a,b=map(int,input().split())
grp=[list(input()) for _ in range(a)]
ans=[]
for i in range(a-7):
    for j in range(b-7):
        cnt1,cnt2=0,0
        for ii in range(i,i+8):
            for jj in range(j,j+8):
                if (ii+jj)%2==1:
                    if grp[ii][jj]=='W':
                        cnt1+=1
                if (ii+jj)%2==0:
                    if grp[ii][jj]=='B':
                        cnt1+=1
                if (ii+jj)%2==1:
                    if grp[ii][jj]=='B':
                        cnt2+=1
                if (ii+jj)%2==0:
                    if grp[ii][jj]=='W':
                        cnt2+=1                    
        ans.append(min(cnt1,cnt2)) 
print(min(ans))
                    