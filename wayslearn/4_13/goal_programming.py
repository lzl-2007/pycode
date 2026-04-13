import numpy as np

'''                                                #这是原本的整数规划
import pulp as pp
model=pp.LpProblem("singlegoal",pp.LpMaximize)
x1=pp.LpVariable("产品一",lowBound=0,cat="integer")
x2=pp.LpVariable("产品二",lowBound=0,cat="integer")
model+=8*x1+10*x2
model+=2*x1+x2<=11
model+=x1+2*x2<=10
model.solve()
print(pp.LpStatus)
print(x1.varValue)
print(x2.varValue)
print(pp.value(model.objective))
'''
#试着多目标规划
import pulp as pp
model=pp.LpProblem("多目标规划",pp.LpMaximize)
xs=np.array([[pp.LpVariable(f"{i} {j}",lowBound=0,cat="integer") for i in range(2) ]for j in range(3)])
matrix=np.array([
    [2,2,12],
    [4,0,16],
    [0,5,15],
    [200,300,0]
])
x1=xs[0,0]*2+xs[1,0]*4
x2=xs[0,1]*2+xs[2,1]*5
model+=pp.lpSum([xs[i,j]/matrix[i,j]*matrix[3,j]for i in range(3) for j in range(2)])
model+=pp.lpSum([xs[i,j]/matrix[i,j]*matrix[3,j]for i in range(3) for j in range(2)])>=1500
model+=xs[0,0]*2+xs[0,1]*2<=12
model+=2*x1-x2<=3
model+=2*x1-x2>=-3
model+=xs[2,0]+xs[2,1]<=20
model+=xs[1,0]+xs[1,1]<=20
model+=xs[1,0]+xs[1,1]>=12
model.solve()
result=np.array([[xs[i,j].varValue for j in range(2)]for i in range(3)])
print(result)
print(pp.lpSum([result[i,j]/matrix[i,j]*matrix[3,j]for i in range(3) for j in range(2)]))