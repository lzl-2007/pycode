import numpy as np                               #实现kruskal的关键：判定联通
from collections import defaultdict
class Simplegraph():            #对象式编程
    def __init__(self,n):
        self.n=n
        self.parent=[i for i in range(n)]
        self.graph=defaultdict(list)

    def judge(self,x,y):
        return (self.parent[x]==self.parent[y])
    

    def union(self,x,y):                                #所有的相同父节点的点都要一起刷新
        if self.parent[x]<self.parent[y]:
            temp=self.parent[y]
            for i in range(self.n):
                if self.parent[i]==temp:
                    self.parent[i]=self.parent[x]
        else:
            temp=self.parent[x]
            for i in range(self.n):
                if self.parent[i]==temp:
                    self.parent[i]=self.parent[y]
        print(self.parent)
        return 0
    
    def add_edge(self,u,v,w):
        self.graph[u-1].append((v-1,w))
        self.graph[v-1].append((u-1,w))
        self.union(u-1,v-1)
        return 0                    
'''
graph=Simplegraph(6)
graph.add_edge(1,2,3)
graph.add_edge(2,5,4)
graph.add_edge(3,5,7)
graph.add_edge(4,6,8)
print(graph.graph)
for i in range(graph.n):
    for j in range(i+1,graph.n):
            if graph.judge(i,j):
                print(f"{i+1}and{j+1}之间联通")
            else:
                 print(f"{i+1}and{j+1}之间不联通")
'''
graph=Simplegraph(4)
graph.add_edge(1,2,1)  # union(0,1): parent=[0,0,2,3]
graph.add_edge(3,4,1)  # union(2,3): parent=[0,0,2,2]
graph.add_edge(2,3,1)  # union(1,2): parent[1]=min(0,2)=0, parent[2]=0 → parent=[0,0,0,2]

# 此时：节点4(索引3)的parent[3]=2，节点3(索引2)的parent[2]=0
print(graph.graph)
for i in range(graph.n):
    for j in range(i+1,graph.n):
            if graph.judge(i,j):
                print(f"{i+1}and{j+1}之间联通")
            else:
                 print(f"{i+1}and{j+1}之间不联通")

    
