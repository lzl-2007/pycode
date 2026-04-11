from collections import defaultdict
'''
#尝试prime算法
graph=defaultdict(list)

def prime(graph,n):
    A=set()
    A.add(0)
    while (len(A)<n):
        temp=[float('inf'),0,0]
        for u,neighbour in graph.items():
            for v,weight in neighbour:
                if (u not in A) or (v in A):
                    continue
                judge1=(temp[0]<=weight)
                judge2=(temp[0]>weight)
                temp=[min(temp[0],weight),u*judge2+temp[1]*judge1,v*judge2+temp[2]*judge1]
        A.add(temp[2])
        print(f"{temp[1]+1}-{temp[2]+1}")
    return 0

def add(u,v,weight):
    graph[u-1].append((v-1,weight))
    graph[v-1].append((u-1,weight))
    return 0
add(1,2,50)
add(1,3,60)
add(2,4,65)
add(2,5,40)
add(3,4,52)
add(3,7,45)
add(4,5,50)
add(4,6,30)
add(4,7,42)
add(5,6,70)
print(graph)
prime(graph,7)#成功的prime算法
'''



