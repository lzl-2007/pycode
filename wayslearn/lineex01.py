import numpy as np
from scipy.optimize import linprog

def model(form,n=2,M=1,a=0.1):
    c=form[:,0]
    c=-np.insert(c,0,5)/100
    c=np.insert(c,n+1,0)
    A_ub=np.array([[0] for _ in range(n+2) ]).reshape(1,n+2)
    for i in range(n):
        A_ub[0,i+1]=form[i,2]+1
    b_ub=np.array([0 for _ in range(n+2)])
    b_ub[0]=M
    b_ub[n+1]=M*a
    totack=np.zeros([n+1,n+2])
    for i in range(n):
        totack[i,i+1]=form[i,1]
        totack[i,n+1]=-1
    totack[n,n+1]=1
    A_ub=np.concatenate([A_ub,totack],axis=0)
    bounds=np.array([(0,None) for _ in range(n+2)])
    result=linprog(c,A_ub=A_ub,b_ub=b_ub,bounds=bounds,method="highs")
    if result.success:
        for i in range(0,n+1):
            print(f"x{i}={result.x[i]}")
        print(result.fun)
    else:
        print(result.message)
    return 0

form=np.array([[28,2.5,1,103],
      [21,1.5,2,198],
      [23,5.5,4.5,52],
      [25,2.6,6.5,40]])
model(form,4,1,0.006)
