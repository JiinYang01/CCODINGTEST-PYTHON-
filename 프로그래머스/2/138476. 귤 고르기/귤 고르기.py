from collections import Counter
def solution(k, tangerine):
    answer = 0
    p=[]
    z=0
    x=list(set(tangerine))
    p=list(Counter(tangerine).values())
    p.sort(reverse=True)
    for q,l in enumerate(p):
        z=z+l
        answer=answer+1
        if z>=k:
            break
    return answer


