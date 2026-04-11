import numpy as np
from collections import defaultdict
graph=defaultdict(list)
S=np.array([
    [1,1,1,1],
    [1,1,1,0],
    [1,1,0,1],
    [1,0,1,1],
    [1,0,1,0],
    [0,1,0,1],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1],
    [0,0,0,0],
])
change=np.array([
    [1,0,0,0],
    [1,1,0,0],
    [1,0,1,0],
    [1,0,0,1]
])
def forkey(a,n):
    for i in range(n):
        judge=1
        for j in range(4):
            if a[j]!=S[i][j]:
                judge=0
        if judge==1:
            return i
def cal(x,y):
    return (x+y)%2

for i in S:
    for j in change:
        if (S==cal(i,j)).all(axis=1).any():
            graph[tuple(i)].append((cal(i,j),1))

def floyd(A0):
    n=A0.shape[0]
    A=np.array([[[float('inf') for _ in range(n)]for i in range(n)]for j in range(n+1)])
    for i in range(n):
        for j in range(n):
            A[0][i,j]=A0[i,j]
    for k in range(0,n):
        for i in range(n):
            for j in range(n):
                A[k+1][i,j]=min(A[k][i,j],A[k][i,k]+A[k][k,j])
    t=9
    while(t>0):
        for i in range(t,0,-1):
            if A[i][0,t]<A[i-1][0,t]:
                print(S[i-1])
                print(i)
                t=i-1
                break
    return A[n]
def makematrix(graph,n):
    matrix=np.array([[float('inf') for i in range(n)]for j in range(n)])
    for u,neighbour in graph.items():
        for v,weight in neighbour:
            i=forkey(u,n)
            j=forkey(v,n)
            matrix[i,j]=weight
    return matrix

A=floyd(makematrix(graph,10))
print(A[0,9])
