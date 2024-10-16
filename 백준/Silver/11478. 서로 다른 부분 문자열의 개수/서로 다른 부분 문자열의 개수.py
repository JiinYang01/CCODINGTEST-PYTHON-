a=input()
a=list(a)
ans=[]
s=''
for i in range(len(a)):
    s=''
    s+=a[i]
    ans.append(s)
    for j in a[i+1:]:
        s+=j
        ans.append(s)
print(len(set(ans)))
