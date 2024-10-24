a=int(input())
x=list(map(int,input().split()))
ans=[]
def bin_search(x):
        global ans
        start=0
        end=len(x)-1
        ans=[x[start],x[end]]
        if x[end]+x[start]==0:
                    return ans       
        while start<end:
            if abs(x[end]+x[start])<abs(ans[0]+ans[1]):
                ans[0]=x[start]
                ans[1]=x[end]
                if x[end]+x[start]==0:
                    break
            if x[end]+x[start]>0:
                 end-=1
            else:
                 start+=1
        return ans

print(sum(bin_search(x)))      