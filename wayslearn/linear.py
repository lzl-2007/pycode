import numpy as np
from scipy.optimize import linprog
import pandas as pd
''' ex1
c=[-2,-3,5]
left=[[1,1,1],
      [-1,-1,-1],
      [-2,5,-1],
      [1,3,1]
      ]
right=[7,-7,-10,12]

bounds=[(0,None),
        (0,None),
        (0,None)]

result=linprog(c,A_ub=left,b_ub=right,bounds=bounds,method="highs")
if result.success:
    print(f"{result.x[0]}  {result.x[1]}  {result.x[2]}")
    print(-result.fun)
    '''

'''
c=[2,3,1]
A_ub=[[-1,-4,-2],
      [-3,-2,0]]
b_ub=[-8,-6]
bounds=[(0,None),
        (0,None),
        (0,None)]
result=linprog(c,A_ub=A_ub,b_ub=b_ub,bounds=bounds,method="highs")
if result.success:
    print(result.x[0])
    print(result.x[1])
    print(result.x[2])
    print(result.fun)
else: 
    print(result.message)
    '''

c=[1,1,2,2,3,3,4,4]
A=[[1,-1,-1,1],
   [1,-1,1,-3],
   [1,-1,-2,3]]
A_=[[[x,-x] for x in row] for row in A]
A_ub=np.array(A_).reshape(3,8)
b_ub=[-2,-1,-0.5]
bounds=[[0,None] for _ in range(0,8)]
result=linprog(c,A_ub=A_ub,b_ub=b_ub,bounds=bounds,method="highs")

if result.success:
    for i in range(4):
        print(f"x{i+1}的值为{result.x[2*i]-result.x[2*i+1]}")
    print(f"最小值为{result.fun}")
else:
    print(result.message)