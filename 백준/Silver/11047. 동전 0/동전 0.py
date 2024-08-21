x,y=map(int,input().split())
k=[]
for i in range(x):
    d=int(input())
    k.append(d)
k.sort(reverse=True)
l=0
for i in k:
    if y//i>0:
        l+=y//i
    y=y-(y//i*i)
print(l)