def solution(nums):
    answer = 0
    d={}
    for i in nums:
        d[i]=0
    for i in nums:
        d[i]+=1
    a=sorted(list(d.values()))
    u=len(nums)//2
    if u<len(a):
        answer=u
    else:
        answer=len(a)
        
    
    
    
    
    return answer