import numpy as np
import matplotlib.pyplot as plt

'''
data=np.array([
    [19,25,31,38,44],
    [19,32.3,49,73.3,97.8]
])

x=data[0,:]
y=data[1,:]

result=np.polyfit(x,y,deg=2)               #二次拟合

print(f"{result[0]}x^2+{result[1]}x+{result[2]}")
def func(x):
    return result[0]*x**2+result[1]*x+result[2]
x_=np.linspace(15,45,50)
y_=func(x_)

plt.figure(figsize=[5,5])
plt.plot(x_,y_,color='b',label=f"{result[0]:.3f}x^2+{result[1]:.3f}x+{result[2]:.3f}")
plt.scatter(x,y,marker='*',color="r")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()'''
n=3
N=15
M=10000
randata=np.random.normal(0,1,size=[M,])
x=np.linspace(-2,2,N)
y=np.array([len(randata[(randata<x[i]) & (randata>x[i-1])]) for i in range(1,N)])
y=np.append(y,len(randata[randata>x[N-1]]))
y=y/M
print(y)
result=np.polyfit(x,y,deg=n)
def fun(x,n=3):
    return sum(result[i]*x**(n-i) for i in range(n+1))
from scipy import integrate
ans,error=integrate.quad(fun,-2,2)
x_=np.linspace(-3,3,200)
plt.figure(figsize=[7,7])
plt.plot(x_,fun(x_,n),color='y',label=f"int={ans}")
plt.scatter(x,y,color='r',marker='*')
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()