import sys
input = sys.stdin.readline
a,b=map(int,input().split())
grp=list(map(int,input().split()))
ans=b
st=0
aa=grp[0]
end=0
while st<=end:
    if st>end:
        break
    if st>a or end>a:
        break
    if aa<b:
        if end+1<a:
            aa+=grp[end+1]
        end+=1
    if aa>=b:
        ans=min(ans,end-st+1)
        aa-=grp[st]
        st+=1
if sum(grp)<b:
    print(0)
else:
    print(ans)
