a=int(input())
grp=[0]*1005
grp[1]=1
grp[2]=2
grp[3]=3
for i in range(4,1005):
    grp[i]=grp[i-2]+grp[i-1]
print(grp[a]%10007)