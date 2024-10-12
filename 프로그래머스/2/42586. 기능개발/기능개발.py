from collections import deque
def solution(progresses, speeds):
    answer = []
    grp=[]
    cnt=0
    for i in range(len(progresses)):
        a=(100-progresses[i])//speeds[i]
        if (100-progresses[i])%speeds[i]!=0:
            a+=1
        if grp!=[]:
            if grp[-1]<=a:
                grp.append(a)
            else:
                grp.append(grp[-1])
                answer.append(cnt)
        else:
            grp.append(a)
    d={}
    for i in grp:
        d[i]=0
    for i in grp:
        d[i]+=1
    answer=list(d.values())
    return answer