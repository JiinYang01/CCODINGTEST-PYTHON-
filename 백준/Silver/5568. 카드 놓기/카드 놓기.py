from itertools import permutations
a=int(input())
b=int(input())
grp=[]
for i in range(a):
    d=(input())
    grp.append(d)
ans=[]
s=list(permutations(grp,b))
for i in s:
    aa=''
    for k in i:
        aa+=k
    ans.append(aa)
print(len(set(ans)))