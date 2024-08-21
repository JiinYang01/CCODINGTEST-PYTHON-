a,b=map(int,input().split())
x=list(map(int,input().split()))
pr=[0]*(a+1)
m=[]
for i in range(a):
    pr[i + 1] = pr[i] + x[i]
for l in range(b):
    x1,x2=map(int,input().split())
    k=pr[x2]-pr[x1-1]
    m.append(k)
for i in m:
    print(i)