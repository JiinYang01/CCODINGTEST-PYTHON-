from collections import deque
def solution(priorities, location):
    answer = 0
    a=0
    ans=[]
    k=sorted(priorities,reverse=True)
 
    s=0
    while a<len(priorities):
        i=0
        for i in range(len(priorities)):
            if priorities[i]==k[s]:
                ans.append(i)
                a+=1
                s+=1
            if s==len(k):
                break
        if a==len(priorities):
            break
    answer=ans.index(location)+1
    return answer