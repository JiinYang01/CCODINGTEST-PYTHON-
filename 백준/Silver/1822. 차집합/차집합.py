a,b=map(int,input().split())
x=set(list(map(int,input().split())))
y=set(list(map(int,input().split())))
ans=sorted(list(x-y))
if ans==[]:
    print(0)
else:
    print(len(ans))
    print(*ans)
