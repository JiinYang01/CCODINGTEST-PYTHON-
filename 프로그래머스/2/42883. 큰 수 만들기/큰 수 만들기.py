def solution(number, k):
    answer = ''
    x=list(number)
    s=[]
    if len(number)-k>1:
        s.append(x[0])
    else:
        s.append(max(x))    
    if  len(number)-k>1:
            for i in x[1:]:
                if i>s[-1] and k>0:
                    while s and s[-1]<i and k>0:
                        s.pop()
                        k-=1
                    s.append(i)
                else:
                    s.append(i)
    if k==1:
        s.pop()
    for i in s:
        answer+=i
            
        
    return answer