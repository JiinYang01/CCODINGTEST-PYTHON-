from itertools import combinations
def solution(clothes):
    answer = 1
    d={}
    a=[]

    for i in clothes:
        d[i[1]]=[]
    for i in clothes:
        d[i[1]].append(i[0])
    m=list(d.values())
    for i in m:
        a.append(len(i))
    for i in a:
        answer=answer*(i+1)
    answer-=1
    return answer