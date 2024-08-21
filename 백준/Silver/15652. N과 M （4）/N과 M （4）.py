a,b=map(int,input().split())
grp=[_ for _ in range(1,a+1)]
stack=[]
def dfs(depth):
    if depth==b:
        print(*stack)
        return
    if depth==0:
        for i in grp:
            stack.append(i)
            dfs(depth+1)
            stack.pop()
                
    for i in grp:
        if depth!=0:
            if i>=stack[-1]:
                stack.append(i)
                dfs(depth+1)
                stack.pop()
      
            

dfs(0)