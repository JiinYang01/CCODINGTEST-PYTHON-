s=input()
i=len(s)//2

t=s[0]
if t*len(s)==s:
    ans=(len(s))
elif s[:i]==s[len(s)-1:i-1:-1]:
    ans=(len(s))
else:
    while i<len(s):
        b=s[i+1:]
        a=s[i::-1]
        c=s[i-1::-1]
        if a[:len(b)]!=b and c[:len(b)]!=b:
            i+=1
        else:
            break

    if i+1==len(s):
        ans=(len(s)*2-1)
    else:
        if a[:len(b)]==b:
            o=a[:len(b)]
            ans=(i*2+2)
        if c[:len(b)]==b:
            ans=(i*2+1)

print(ans)