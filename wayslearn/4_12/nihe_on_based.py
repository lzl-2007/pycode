import numpy as np

'''
pi=np.pi
X=np.linspace(-pi/2,pi/2,30)
Y=np.cos(X)

def make_A(x):
    return [np.ones_like(x),x**2,x**4]

A=np.array(make_A(X))
A=np.transpose(A)

B=np.linalg.lstsq(A,Y)          #通过取出样本构造多元一次方程，求出最小二乘解，即可得到系数
print(B)
print(A.shape)
'''
#一个具体的例子
sediment_concentration = np.array([
    32, 60, 75, 85, 90, 98, 100, 102, 108, 112, 115, 116,
    118, 120, 118, 105, 80, 60, 50, 30, 26, 20, 8, 5
])
water_flow = np.array([
    1800, 1900, 2100, 2200, 2300, 2400, 2500, 2600, 2650, 2700, 2720, 2650,
    2600, 2500, 2300, 2200, 2000, 1850, 1820, 1800, 1750, 1500, 1000, 900
])
t=np.linspace(3600*8,3600*8+3600*24*11.5,24)
sediment_away=np.array([sediment_concentration[i]*water_flow[i] for i in range(24)])
from scipy.interpolate import interp1d
import scipy.integrate
func1=interp1d(t,sediment_away,kind="cubic")

def func(x):
    return func1(x)
print(func(t))

import matplotlib.pyplot as plt
'''
result,error=scipy.integrate.quad(func,a=3600*8,b=3600*8+3600*24*11.5)
plt.figure(figsize=[10,10])
x=np.linspace(3600*8,3600*8+3600*24*11.5,200)
plt.plot(x,func(x),color='y',label=f"{result:.4e}")
plt.scatter(t,sediment_away,marker='*',color="r")
plt.vlines(x=3600*8,ymax=func(3600*8),ymin=0)
plt.vlines(x=3600*8+3600*24*11,ymax=func(3600*8+3600*24*11),ymin=0)
                                                                                  #勉强成功的一次拟合积分

plt.legend()
#plt.show()

'''

fig,(ax1,ax2)=plt.subplots(1,2,figsize=[10,5])
water1=water_flow[:11]
water2=water_flow[11:]
sediment1=sediment_away[:11]
sediment2=sediment_away[11:]

result,resuduals,_,_,_=np.polyfit(water1,sediment1,deg=1,full=True)
def fun(x):
    return result[0]*x+result[1]
x=np.linspace(water1[0],water1[-1],100)
y=fun(x)
ax1.plot(x,y,color='y',label=f"y={result[0]:.4f}x+{result[1]:.4e},residuals={resuduals[0]:.2e}")
ax1.scatter(water1,sediment1,color='r')
ax1.legend()
minresi=[float('inf'),0]
for i in [2,3,4]:
    coffe,resi,_,_,_=np.polyfit(water2,sediment2,deg=i,full=True)
    judge=(resi<minresi[0])
    minresi=[min(minresi[0],resi),judge*i+minresi[1]*(resi>=minresi[0])]
n=minresi[1][0]
coffe,resi,_,_,_=np.polyfit(water2,sediment2,deg=n,full=True)
def fun2(x):
    return sum(coffe[j]*x**(n-j) for j in range(n+1))
x2=np.linspace(water2[0],water2[-1],100)
y2=fun2(x2)
ax2.plot(x2,y2,color="y",label='+'.join([f"{coffe[k]:.1e}x^{n-k}" for k in range(n+1)]))#成功的表达和拟合
ax2.scatter(water2,sediment2)
plt.legend()
plt.show()
