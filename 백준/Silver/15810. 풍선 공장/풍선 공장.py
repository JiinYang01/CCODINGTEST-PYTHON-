a,b=map(int,input().split())
grp=list(map(int,input().split()))
k=min(grp)
st=1
end=k*b
while st+1<end:
    cnt=0
    mid=(st+end)//2
    for i in grp:
        cnt+=mid//i
    if cnt>=b:
        end=mid
    else: 
        st=mid
print(end)