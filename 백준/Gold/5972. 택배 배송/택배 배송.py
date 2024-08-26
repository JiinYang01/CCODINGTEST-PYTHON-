import heapq

a,b=map(int,input().split())
grp=[[] for _ in range(a+1)]
INF=1e8
distance=[INF]*(a+1)
for i in range(b):
    x,y,z=map(int,input().split())
    grp[x].append((y,z))
    grp[y].append((x,z))

def dijkstra(start):
    distance[start]=0
    q=[]
    heapq.heappush(q,(0,start))
    while q:
        dist,node=heapq.heappop(q)
        if dist>distance[node]:
            continue
        for i in grp[node]:
            if i[1]+dist<distance[i[0]]:
                distance[i[0]]=i[1]+dist
                heapq.heappush(q,(i[1]+dist,i[0]))


dijkstra(1)
print(distance[a])