import numpy as np
import networkx as nx
import matplotlib.pyplot as plt 

'''
G=nx.DiGraph()              #nx的最短路径解法
def add(u,v,w):
    G.add_edge(u,v,weight=w)
    return 0
add(0,1,4)
add(0,2,2)
add(1,2,3)
add(1,3,2)
add(1,4,6)
add(2,3,5)
add(2,5,4)
add(3,4,2)
add(3,5,7)
add(4,5,4)
add(4,6,8)
add(5,6,3)
print(G)
plt.figure(figsize=[8,4])
pos=nx.spring_layout(G)
nx.draw(G,pos=pos,with_labels=True)
labels=nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos=pos,edge_labels=labels)
plt.axis('off')
#plt.show()

path=nx.shortest_path(G,source=0,target=6,weight='weight')
length=nx.shortest_path_length(G,source=0,target=6,weight='weight')
print(path)
print(length)'''

'''
import networkx as nx

# 创建无向图                              #生成最小树
G = nx.Graph()
edges = [(1, 2, 50), (1, 3, 60), (2, 4, 65), (2, 5, 40),
         (3, 4, 52), (3, 7, 45), (4, 5, 50), (4, 6, 30),
         (4, 7, 42), (5, 6, 70)]

for u, v, w in edges:
    G.add_edge(u, v, weight=w)

# 最小生成树
mst = nx.minimum_spanning_tree(G, weight='weight')
total_weight = mst.size(weight='weight')

print(f"总权重: {total_weight}")  # 257
print(f"边: {list(mst.edges(data=True))}")
'''

 