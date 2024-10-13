def solution(s):
    answer = True
    a=[]
    if s[0]==')':
        return False
    else:
        for i in s:
            if i=='(':
                a.append(i)
            elif i==')':
                if a!=[]:
                    a.pop()
                else:
                    return False
    if a==[]:
        return True
    else:
        return False
    return True