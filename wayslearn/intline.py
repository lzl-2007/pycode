import pulp as pp
import numpy as np
'''
model=pp.LpProblem("生产计划",pp.LpMaximize)
x1=pp.LpVariable("产品1",lowBound=0,cat="Integer")
x2=pp.LpVariable("产品2",lowBound=0,cat="Integer")

model+=40*x1+30*x2
model+=2*x1+x2<=100
model+=x1+3*x2<=120
model.solve()

print(pp.LpStatus[model.status])
print(x1.varValue)
print(x2.varValue)
print(pp.value(model.objective))
'''
'''
model=pp.LpProblem("0-1背包",pp.LpMaximize)
x=[pp.LpVariable(f"第{i}种",cat="Binary") for i in range(6)]
A=np.array([6,4,2,3,1,1])
B=np.array([25,15,10,12,8,6])
model+=pp.lpSum(B[i]*x[i] for i in range(6))
model+=pp.lpSum(A[i]*x[i] for i in range(6))<=10
model.solve()
print(pp.LpStatus[model.status])
print([x[i].varValue for i in range(6)])
print(pp.value(model.objective))
'''

def assign(matrix,n):
    model=pp.LpProblem("指派问题",pp.LpMinimize)
    x=[[pp.LpVariable(f"{i}{j}",cat="Binary") for i in range(n)]for j in range(n)]
    model+=pp.lpSum(x[i][j]*matrix[i,j] for i in range(n) for j in range(n))
    for i in range(n):
        model+= pp.lpSum(x[i][j] for j in range(n))==1
    for j in range(n):
        model+= pp.lpSum(x[i][j] for i in range(n))==1
    
    

    model.solve()
    print(pp.LpStatus[model.status])
    print([[x[i][j].varValue for i in range(n)] for j in range(n)])
    print(pp.value(model.objective))
    return 0

matrix=np.array([[3,8,2,10,3],
        [8,7,2,9,7],
        [6,4,2,7,5],
        [8,4,2,3,5],
        [9,10,6,9,10]])
assign(matrix,5)
