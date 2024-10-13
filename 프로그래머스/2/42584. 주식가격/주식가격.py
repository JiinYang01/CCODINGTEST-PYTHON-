def solution(prices):
    answer = []
    q=[]
    for i in range(len(prices)):
        x=0
        for j in range(i+1,len(prices)):
            if i==len(prices)-1:
                break
            if prices[i]<=prices[j]:
                x+=1
            else:
                x+=1
                break

        answer.append(x)
    return answer