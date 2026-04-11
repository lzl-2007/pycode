import numpy as np

def floyd(A0):
    n=A0.shape[0]
    A=np.array([[[float('inf') for _ in range(n)]for __ in range(n)]for i in range(2)])
    for i in range(n):
        for j in range(n):
            A[0][i,j]=A0[i,j]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                A[((k+1)%2)][i][j]=min(A[(k%2)][i][j],A[(k%2)][i,k]+A[(k%2)][k,j])
    return A[((k+1)%2)]

A0=np.array([
    [0,50,float('inf'),40,25,10],
    [50,0,15,20,float('inf'),25],
    [float('inf'),15,0,10,20,float('inf')],
    [40,20,10,0,10,25],
    [25,float('inf'),20,10,0,55],
    [10,25,float('inf'),25,55,0]
])
print(A0.shape)
print(floyd(A0))#  比较好看的floyd算法



