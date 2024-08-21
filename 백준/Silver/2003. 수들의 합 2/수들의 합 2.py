from itertools import combinations
a,b=map(int,input().split())
x=list(map(int,input().split()))
j=[0]*(a+1)
for i in range(a):
    j[i+1]=j[i]+x[i]
a=combinations(j,2)
cnt=0
for i in a:
    if (i[1]-i[0])==b:
       cnt+=1
print(cnt) 