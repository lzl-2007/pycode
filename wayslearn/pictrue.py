from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt

'''              图的构建和显示
def add(v,neighbour,weigh):
    gragh[v].append((neighbour,weigh))
    gragh[neighbour].append((v,weigh))
    return 0
add(0,1,5)
add(0,3,3)
add(1,2,2)
add(2,3,1)

print([gragh[x] for x in range(4)])

G=nx.Graph()

for v,neighbour in gragh.items():
    for u,weigh in neighbour:
        G.add_edge(v,u,weigh=weigh)
print(G)
plt.figure(figsize=(8,6))
pos=nx.spring_layout(G)
nx.draw(G,pos,with_labels=True)
labels = nx.get_edge_attributes(G, 'weigh')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.axis('off')
plt.show()'''

def makegraph(matrix,n):
    graph=defaultdict(list)
    for i in range(n-1):
        for j in range(i+1,n):
            if matrix[i][j]<float('inf'):
                graph[i].append((j,matrix[i][j]))
                graph[j].append((i,matrix[i][j]))
    
    return graph
dp=[[float('inf') for _ in range(11)] for __ in range(11)]
def find_short(graph,start,target=0,n=11):
    
    for u,neighbour in graph.items():
        for v,weigh in neighbour:
            dp[u][v]=weigh
    
    for i in range(n):
        dp[i][i]=0
    
    for i in range(1,n):
        temp=float('inf')
        for j in range(n):
            dp[start][start-i]=min(dp[start][start-i],dp[start][start-i+j]+dp[start-i+j][start-i])
    print(dp)
    return dp[start][target],dp

judge=1
def far(graph,n):
    while(1):
        for i in range(n):
            find_short(graph,start=i,n=n)
        for i in range(n):
            for j in range(n):
                if dp[i][j]==float('inf'):
                    judge=0
        if judge==1:
            break

'''
matrix=[
    [0,50,float('inf'),40,25,10],
    [50,0,15,20,float('inf'),25],
    [float('inf'),15,0,10,20,float('inf')],
    [40,20,10,0,10,25],
    [25,float('inf'),20,10,0,55],
    [10,25,float('inf'),25,55,0]
]
graph=makegraph(matrix,6)
for i in range(5):
    print(find_short(graph,0,i+1,6))    #半动态规划的自编算法'''
def showway(graph,start,target,n):
    num,dp=find_short(graph,start,target,n)
    def circle(a,b):
        for u,neighbour in graph.items():
            for v,weight in neighbour:
                if a==u & weight<float('inf'):
                    if dp[a][b]==weight+dp[v][b]:
                        print(f"{u}--{v}")
                        break
        circle(v,b)
        return 0
    return dp[start][target]

graph=defaultdict(list)
def add(u,v,weight):
    graph[u].append((v,weight))
    graph[v].append((u,weight))
    return 0

add(1,2,2)
add(2,5,1)
add(3,5,5)
add(2,3,6)
add(1,3,8)
add(1,4,1)
add(3,4,7)
add(4,7,9)
add(3,7,2)
add(3,6,1)
add(4,7,9)
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
graph2=defaultdict(list)
for u,neighbour in graph.items():
    for v,weight in neighbour:
        graph2[u-1].append((v-1,weight))
far(graph2,11)

print(showway(graph2,0,10,11))#错误的方法，不够好


