from collections import deque
def solution(numbers, target):
    answer = 0
    q=deque()
    q.append([numbers[0],0])
    q.append([numbers[0]*(-1),0])
    while q:
        tmp,idx=q.popleft()
        if idx<len(numbers)-1:
                idx=idx+1
                q.append([tmp+numbers[idx],idx])
                q.append([tmp-numbers[idx],idx])
        else:
            if tmp==target:
                answer+=1
    return answer