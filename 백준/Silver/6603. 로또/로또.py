def dfs(depth):
    if depth==6:
        print(*stack)
        return

    if depth==0:
        for i in grp:
            stack.append(i)
            dfs(1)
            stack.pop()

    for i in grp:
        if i not in stack and depth!=0: 
            if i>stack[-1]:
                stack.append(i)
                dfs(depth+1)
                stack.pop()

while True:
    grp=list(map(int,input().split()))
    V=grp.pop(0)
    if V==0:
        exit()
    stack=[]
    dfs(0)
    print()