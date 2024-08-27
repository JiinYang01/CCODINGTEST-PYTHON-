x=int(input())
s=input()
grp=[]
a=s[0]
for i in s[1:]:
    if i==a[0]:
        a+=i
    else: 
        grp.append(a)
        a=i
grp.append(a) 
rcnt=0
bcnt=0
cnt=0
cnt1=0

if grp[0][0]=='B' and grp[len(grp)-1][0]=='B':
    if grp[0][0]=='B':
        for i in grp[1:]:
            if i[0]=='B':
                cnt+=len(i)
    if grp[len(grp)-1][0]=='B':
                for i in grp[:len(grp)-1]:
                    if i[0]=='B':
                        cnt1+=len(i)
    bcnt=min(cnt,cnt1)
if grp[0][0]=='B' and grp[len(grp)-1][0]!='B':
    if grp[0][0]=='B':
        for i in grp[1:]:
            if i[0]=='B':
                bcnt+=len(i)   
if grp[0][0]!='B' and grp[len(grp)-1][0]=='B':
     if grp[len(grp)-1][0]=='B':
                for i in grp[:len(grp)-1]:
                    if i[0]=='B':
                        bcnt+=len(i)
if grp[0][0]!='B' and grp[len(grp)-1][0]!='B':
        for i in grp[:len(grp)-1]:
                    if i[0]=='B':
                        bcnt+=len(i)




     
cntt=0
cnt11=0

if grp[0][0]=='R' or grp[len(grp)-1][0]=='R':
    if grp[0][0]=='R':
        for i in grp[1:]:
            if i[0]=='R':
                cntt+=len(i)
    if grp[len(grp)-1][0]=='R':
            for i in grp[:len(grp)-1]:
                    if i[0]=='R':
                        cnt11+=len(i)                 
    rcnt=min(cntt,cnt11)
if grp[0][0]=='R' and grp[len(grp)-1][0]!='R':
    if grp[0][0]=='R':
        for i in grp[1:]:
            if i[0]=='R':
                rcnt+=len(i)   
if grp[0][0]!='R' and grp[len(grp)-1][0]=='R':
     if grp[len(grp)-1][0]=='R':
                for i in grp[:len(grp)-1]:
                    if i[0]=='R':
                        rcnt+=len(i)
if grp[0][0]!='R' and grp[len(grp)-1][0]!='R':
    for i in grp[:len(grp)-1]:
                if i[0]=='R':
                    rcnt+=len(i)
    
print(min(rcnt,bcnt))
