a=int(input())
x=list(map(int,input().split()))
k=sorted(x)
k=sorted(list(set(k)))
d={}
jj=0
for i in k:
    d[i]=jj
    jj+=1
ans=[]

for i in range(len(x)):
    ans.append(d[x[i]])
print(*ans)
    