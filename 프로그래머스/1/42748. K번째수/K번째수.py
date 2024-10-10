def solution(array, commands):
    answer = []
    for i in commands:
        x=array[i[0]-1:i[1]]
        x.sort()
        
        answer.append(x[i[2]-1])
    return answer