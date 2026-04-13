import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import step, lti,lsim
sys=lti([1],[2,1])
ts=np.linspace(0,20,200)
u=ts
t,y,_=lsim(sys,U=u,T=ts)
plt.plot(t, y, 'b-', linewidth=2, label='系统输出 y(t)')
plt.grid(True)
plt.xlabel("时间t")
plt.ylabel("输出y")
plt.legend()
plt.show()