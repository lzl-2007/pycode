from collections import defaultdict
import numpy as np

graph=defaultdict(list)
def add(u,v,w):
    graph[u-1].append((v-1,w))
    graph[v-1].append((u-1,w))
    return 0
add(1,2,2)
add(1,3,4)
add(2,4,3)
add(2,5,3)
add(2,6,1)
add(3,4,2)
add(3,5,3)
add(3,6,1)
add(4,7,1)
add(5,7,3)
add(6,7,4)

'''
#直接采用简单的库函数
import networkx as nx
G=nx.Graph()
for u,neighbour in graph.items():
    for v,w in neighbour:
        G.add_edge(u,v,weight=w)
        
def find_short(G,A,B):
    result=nx.shortest_path(G,A,B)
    print(result)
    print(nx.shortest_path_length(G,A,B,weight='weight'))   #要加上权重，否则会只算边数
    
find_short(G,0,6)
print(graph)'''

#尝试使用kijkstra算法实现
import heapq as pq
start=0
heap=[(0,start)]
A=set()
n=0
for u,nei in graph.items():
    n+=1
dist=[float('inf') for _ in range(n)]

while heap:
    u,d=pq.heappop(heap)
    if (u in A):
        continue
    dist[u]=d
    A.add(u)
    for v,w in graph[u]:
        if dist[v]>d+w:
            dist[v]=d+w
            pq.heappush(heap,(v,dist[v]))
print(dist)
#√ 有效的kijkstra实现

#尝试回溯寻找路径
'''
target=6
aim=target

while (1):

    dis=[float('inf') for _ in range(n)]
    dis[start]=0
    hea=[(0,start)]
    while hea:
        
        
        u,d=pq.heappop(hea)
        if (u in A):
            continue
        dis[u]=d
        A.add(u)
        for v,w in graph[u]:
            if dis[v]>d+w:
                dis[v]=d+w
                if (v==start and dis[v]==dist[v]):
                    print(f"-{v}-")
                    aim=v
                    break
                pq.heappush(hea,(v,dis[v]))
    if aim==start:
        break
'''                                   #失败的尝试