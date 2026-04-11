from collections import defaultdict
graph=defaultdict(list)

def add(u,v,weight):
    graph[u-1].append((v-1,weight))
    graph[v-1].append((u-1,weight))
    return 0
'''
add(1,2,5)
add(1,3,2)
add(2,3,1)
add(2,4,1)
add(3,4,4)

n=4
'''

add(1,2,2)#
add(2,5,1)#
add(3,5,5)#
add(2,3,6)#
add(1,3,8)#
add(1,4,1)#
add(3,4,7)#
add(4,7,9)#
add(3,7,2)#
add(3,6,1)#
add(5,6,3)
add(6,7,4)
add(5,8,2)
add(5,9,9)
add(6,9,6)
add(9,7,3)
add(7,10,1)
add(8,9,7)
add(9,10,1)
add(8,11,9)
add(9,11,2)
add(10,11,4)
'''
n=11
dic=[[float('inf'),0] for _ in range(n)]
dic[0]=[0,1]
while (1):
    for i in range(n):
        if dic[i][1]==0:
            continue
        for v,weight in graph[i]:
            dic[v][0]=min(dic[i][0]+weight,dic[v][0])
            dic[v][1]=1
    judge=1
    for i in range(n):
        if dic[i][1]==0:
            judge=0
    if judge==1:
        break
print("-----")
for i in range(n):
    for v,weight in graph[i]:
        dic[v][0]=min(dic[i][0]+weight,dic[v][0])
print(dic)
'''
import heapq

def dijkstra(start):                               #较为标准的dijkstra算法
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    pq = [(0, start)]          # (距离, 节点)
    visited = set()

    while pq:
        d, u = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)

        for v, w in graph[u]:
            new_dist = d + w
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v))
    return dist
print(dijkstra(0))
