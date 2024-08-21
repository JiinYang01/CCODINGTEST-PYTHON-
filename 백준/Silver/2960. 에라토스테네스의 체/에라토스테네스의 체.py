x,y=map(int,input().split())
d=[True]*(x+1)
cnt=0

for i in range(2,x+1):
    if d[i]==True:
        cnt+=1
        if cnt==y:
            print(i)
    if d[i]==True:
         j=2
         while i*j<=x:
            if d[i*j]==True:
                 cnt+=1
                 if cnt==y:
                     print(i*j)               
            d[i*j]=False
            j+=1
