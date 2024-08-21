a = int(input())
k = []
for i in range(a):
    m = []
    a, b = input().split()
    m.append(a)
    m.append(b)
    k.append(m)
u = []
for i in k:
    if i[1] == 'enter':
        u.append(i[0])
    if i[1] == 'leave':
        u.remove(i[0])
u.sort(reverse=True)
for i in u:
    print(i)
