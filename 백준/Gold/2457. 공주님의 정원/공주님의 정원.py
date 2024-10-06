a=int(input())
date=[]

for _ in range(a):
    a,b,c,d=map(int,input().split())
    date.append([100*a+b,100*c+d])
date.sort()

end=0
target=301
cnt=0

while date:
    if target>=1201 or target<date[0][0]:
        break
    for i in range(len(date)):
        if target>=date[0][0]:
            if end<date[0][1]:
                end=date[0][1]
            date.remove(date[0])
        else:
            break
    cnt+=1
    target=end


if target>=1201:
    print(cnt)
else:
    print(0)