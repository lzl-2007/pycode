from scipy.optimize import minimize
import numpy as np
'''
def objective(var):
    x=var[0]
    y=var[1]
    return x**3-y**3+3*x**2+3*y**2-9*x

def unobjective(var):
    return -objective(var)

result=minimize(objective,x0=[0,0],method="BFGS")
result2=minimize(unobjective,x0=[0,0],method="BFGS")

print(result.x[0])
print(result.x[1])
print(result.fun)
print(result2.x[0])
print(result2.x[1])
print(-result2.fun)  #求函数极值

'''
'''#函数零点
from scipy.optimize import root_scalar
def func(x):
    return x**3-x*x+2*x-3
result=root_scalar(func,bracket=[-100,100])

print(f"{result.root:.6f}")'''

'''
def func(var):
    x=var[0]
    y=var[1]
    return 2*x*x-4*x*y+4*y*y-6*x-3*y

def ineq(var):
    return -(var[0]+var[1]-3)

def ineq2(var):
    return -(4*var[0]+var[1]-9)

constraint=[
    {'type':'ineq','fun':ineq},
    {'type':'ineq','fun':ineq2}
]
bounds=[(0,None),
        (0,None)]
result=minimize(func,x0=[1,1],method="SLSQP",bounds=bounds,constraints=constraint)
print(result.x[0])
print(result.x[1])
print(result.fun)                  #minimize默认取大,linpro默认取小
'''

def func(var):
    x1=var[0]
    x2=var[1]
    return np.exp(x1)*(4*x1**2+2*x2**2+4*x1*x2+2*x2+1)
 
def ineq1(var):
    x1=var[0]
    x2=var[1]
    return -(x1*x2-x1-x2+1.5)

def ineq2(var):
    x1=var[0]
    x2=var[1]
    return x1*x2+10

bounds=[(None,None),
        (None,None)]

constraint=[
    {'type':'ineq','fun':ineq1},
    {'type':'ineq','fun':ineq2}
]
result=minimize(func,x0=[0,0],bounds=bounds,constraints=constraint,method="SLSQP")
print(result.x[0])
print(result.x[1])
print(result.fun)
