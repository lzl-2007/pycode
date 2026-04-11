from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
'''
x=np.array([0.15,0.16,0.17,0.18])#一元函数的三次样条插值与作图   积分计算
y=np.array([3.5,1.5,2.5,2.8])

y_new=interp1d(x,y,kind='cubic')
x_=np.linspace(0.15,0.18,100)

ans,error=integrate.quad(y_new,0.15,0.18)
plt.figure(figsize=[5,5])
plt.plot(x_,y_new(x_),color='r',label=f"int_ans={ans}  error={error}")
plt.vlines(x=[0.15],ymax=y_new(0.15),ymin=0)
plt.vlines(x=[0.18],ymax=y_new(0.18),ymin=0)
plt.scatter(x,y_new(x),marker='*',color="g")
plt.fill_between(x_,y1=y_new(x_),where=(y_new(x_)>0),color="y")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()'''

from scipy.interpolate import RegularGridInterpolator
from scipy import optimize
from scipy.optimize import minimize
matrix=np.array([
    [636,697,624,478,450],
    [698,712,630,478,420],
    [680,674,598,412,400],
    [662,626,552,334,310]
])
x=np.linspace(100,500,5)
y=np.linspace(100,400,4)
print(x)
print(y)
interp=RegularGridInterpolator(points=(y,x),values=matrix,method='cubic')

def func(var):
    x=var[0]
    y=var[1]
    return -interp(np.array([x,y]))

bounds=[(100,400),
        (100,500)]
result=minimize(func,x0=np.array([200,200]),bounds=bounds,constraints=[])
print(f"{result.x[0]}  {result.x[1]}  {-result.fun}")

x_=np.linspace(100,500,100)              #三维曲面
y_=np.linspace(100,400,100)
z_=np.array([[interp(np.array([i,j])) for i in y_]for j in x_])
z_=np.reshape(z_,[100,100])
from mpl_toolkits.mplot3d import Axes3D
fig=plt.figure(figsize=[6,6])
ax = fig.add_subplot(111, projection='3d')
surf=ax.plot_surface(x_,y_,z_,cmap='viridis')
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
plt.show()

plt.clf()
con=plt.contour(x_,y_,z_,levels=20)                #等高线作图
plt.clabel(con,inline=True,fontsize=8)
#plt.show()