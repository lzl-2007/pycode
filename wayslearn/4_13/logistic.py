import numpy as np
from scipy import integrate

import numpy as np
from scipy.optimize import curve_fit
# 年份数组
years = np.array([1790, 1800, 1810, 1820, 1830, 1840, 1850, 1860,
                  1870, 1880, 1890, 1900, 1910, 1920, 1930, 1940,
                  1950, 1960, 1970, 1980, 1990, 2000])

# 人口数组（单位：百万）
population = np.array([3.9, 5.3, 7.2, 9.6, 12.9, 17.1, 23.2, 31.4,
                       38.6, 50.2, 62.9, 76.0, 92.0, 106.5, 123.2, 131.7,
                       150.7, 179.3, 204.0, 226.5, 251.4, 281.4])
def func(t,r,xm):
    return xm/(1+(xm/population[0]-1)*np.exp(-r*(t-years[0])))
initial_guass=[0.01,300]      #初始猜测有助于收敛
result,_=curve_fit(func,years,population,p0=initial_guass)
import matplotlib.pyplot as plt                                #可以实现的对任意函数的拟合
plt.figure(figsize=[8,8])
plt.scatter(years,population,color="r",marker="*")
x=np.linspace(years[0],years[-1]+20,200)
def func2(t):
    r=result[0]
    xm=result[1]
    return xm/(1+(xm/population[0]-1)*np.exp(-r*(t-years[0])))
y=func2(x)
plt.plot(x,y,color='y')
plt.xlabel("x")
plt.ylabel("y")
#plt.show()
print(func2(2010))

