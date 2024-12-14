a=int(input())
grp=list(map(int,input().split()))
st=0
end=0
grpp=[0]*(max(grp)+1)
ans=[0]*a
while st<=end and end<a and st<a:
    if grpp[grp[end]]<1:
        grpp[grp[end]]+=1
        ans[end]=end-st+1
        end+=1
    else:
        grpp[grp[st]]-=1
        st+=1
print(sum(ans))