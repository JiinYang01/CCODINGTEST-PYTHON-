ans=[]
while True:    
    a=input()
    if a=='.':
        break
    k=[]
    for i in a:
        if i=='[' or i==']' or i=='(' or i==')':
            k.append(i)
    if k==[]:
        ans.append('yes')
        continue
    if k!=[]:
        if k[0]==']' or k[0]==')':
            ans.append('no')
            continue
    h=[]
   
    if k!=[]:
        for i in k:
            if i=='[' or i=='(':
                h.append(i)    
            if i==']':
                 if h!=[]:
                    if h[-1]=='[':
                        h.pop()
                    else:
                        h.append(i)
                 else:
                    h.append(i)
            if i==')':
                if h!=[]:
                    if h[-1]=='(':
                        h.pop() 
                    else:
                        h.append(i)
                else:
                     h.append(i)

    if h==[]:
        ans.append('yes')
    else:
        ans.append('no')
for i in ans:
    print(i)