x=int(input())
a=[0]*(46)
a[1]=1
a[2]=1
for i in range(3,46):
    a[i]=a[i-1]+a[i-2]
print(a[x])