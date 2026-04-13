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
'''
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
print(pp.lpSum([result[i,j]/matrix[i,j]*matrix[3,j]for i in range(3) for j in range(2)]))'''#失败的多目标规划
#权重分配难以确定，转化为约束难以控制
#让我们再试一个
import pulp as pp
data=np.array([
    [5,2,6,7,300],
    [3,5,4,6,200],
    [4,5,2,3,400],
    [200,100,450,250,0]
])
model=pp.LpProblem("运输规划",pp.LpMinimize)#先试着将前4个目标作为约束，第5个作为优化目标
num=[[pp.LpVariable(f"用户{_}{__}",lowBound=0,cat="integer") for _ in range(4)]for __ in range(3)]#变量命名需谨慎，不能重复，否则数据冲突
model+=pp.lpSum([num[i][j]*data[i][j] for i in range(3) for j in range(4)]) #这是待优化的运费总数
for j in range(3):
    model+=pp.lpSum([num[j][i] for i in range(4)])<=data[j][4]#row j sum<生产量
model+=pp.lpSum([num[i][3]for i in range(3)])==250
model+=num[2][0]>=100
for i in range(4):
    model+=pp.lpSum([num[j][i]for j in range(3)])>=data[3][i]*0.8#所有用户满足率不低于80%
model.solve()
print(model.status)
print([[num[i][j].varValue for j in range(4)]for i in range(3)])
print(f"运费总数为{pp.lpSum([(num[i][j].varValue)*data[i][j] for i in range(3) for j in range(4)])}")

#勉强合理的多目标规划，但是能实现的目标还是有点太少了
