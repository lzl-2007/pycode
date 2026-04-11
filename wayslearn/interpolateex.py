import numpy as np
from scipy.interpolate import RegularGridInterpolator
from scipy.optimize import minimize
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt 
from scipy.interpolate import griddata 
from scipy.interpolate import LinearNDInterpolator
matrix=np.array([
    [129,7.5,4],
    [140,141.5,8],
    [103.5,23,6],
    [88,147,8],
    [185.5,22.5,6],
    [195,137.5,8],
    [105,85.5,8],
    [157.5,-6.5,9],
    [107.5,-81,9],
    [77,3,8],
    [81,56.5,8],
    [162,-66.5,9],
    [162,84,4],
    [117.5,-33.5,9]
])
points=[(matrix[i][0],matrix[i][1]) for i in range(14)]
values=[matrix[i][2] for i in range(14)]
func=LinearNDInterpolator(points,values)
def func1(var):
    return -func(var)

bounds=[(70,200),
        (-90,150)]
result=minimize(func1,x0=[90,100],bounds=bounds,constraints=[])
print(f"{result.x[0]} {result.x[1]}  {-result.fun}")

x_=np.linspace(-70,200,100)
y_=np.linspace(-90,150,100)
z_=np.array([[func([i,j])for i in x_]for j in y_])
z_=np.reshape(z_,[100,100])
print(z_)
fig=plt.figure(figsize=[8,8])
ax=fig.add_subplot(111,projection='3d')
con=plt.contour(x_,y_,z_,levels=20)
plt.show()
