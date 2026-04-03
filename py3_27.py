import torch
import numpy as np
print(f"1.")
x=torch.arange(4)
y=torch.arange(6,dtype=torch.float32)
print(x)
print(y)


print("2.")
print(torch.empty(3,dtype=torch.int32))
print(torch.zeros(2,3,dtype=torch.float64))
print(torch.randn(2,3))
print(torch.tensor([1,2.4,543]))
print(torch.tensor(np.array([2,4])))

print("3.")
x2=torch.randn(3,4).cuda()
print(x2)
print(x2.device)
print(x2.dim())

print("3.")
x3=torch.tensor([2,3,4,4])
y3=torch.tensor([3,4,5,6])
print(f"{x3+y3}\n{x3-y3}")

print("4.")
x4=torch.range(-10,10,0.1)
y4=torch.tanh(x4)
import matplotlib.pyplot as plt
plt.plot(x4,y4,color="skyblue",linestyle="-",marker=".")

print("5.")
x5=torch.randn(1,3,4,1)
print(x5)
x5_squeeeze=x5.squeeze()
print(x5_squeeeze)
print(x5.shape)
print(x5_squeeeze.shape)
y5=x5_squeeeze.unsqueeze(1)
print(f"{y5}\n{y5.shape}")

print("6.")
x6=torch.tensor([1,2,3])
x6_v=x6.view(3,1)
x6_r=x6.reshape(-1,1)
print(x6_v)
print(x6_r)
y6=torch.rand(2,2)
y6_t=y6.transpose(0,1)#将axis=0、1转置
y6_t2=y6.transpose(1,0)
print(y6)
print(y6_t)
print(y6_t2)
z=torch.randn(3,3)
print(z)
print(np.sort(z,axis=0))#x=0每一列分别排序

print("7.")
w=torch.tensor([[1,2],[1.2,1.6]])
print(w[w>1.6])
print(torch.where(w>1.6,w,torch.tensor(0.0)))#where:条件选择，条件，前者选择，后者选择
x7=torch.randn(3,4)
print(x7)
x7_mask=torch.where(x7>0,x7,torch.tensor(10))
print(x7_mask)

print("8.")
import torch.nn.functional as F
x8=torch.tensor([[1,2],[3,4]])
x8_pad=F.pad(x8,pad=(1,1,1,1),mode='constant',value=0)
print(x8)
print(x8_pad)
y8=torch.randn(3,4)
print(y8)
y8_pad=F.pad(y8,pad=[1,1,0,1],mode='constant',value=10) #import torch.nn.functional,F.pad(处理对象，pad=(左右上下),constant为常数，value给出值)
print(y8_pad)

print("9.")
x9=torch.tensor([[1,2,3,4],[5,6,7,8]])
x9_stride=x9.as_strided(size=(2,2),stride=(4,3))#x_stride[i,j]索引=i*stride[0]+j*stride[1]
print(f"{x9}\n{x9_stride}")

print("10.")
x10=torch.tensor([1,2,3,3]).reshape(2,-1)
y10=torch.tensor([2,2,2,2]).reshape(-1,2)
print(f"{x10}\n{y10}")
print(torch.cat((x10,y10),dim=0))
print(torch.cat((x10,y10),dim=1))#0是纵向拼接，1是横向拼接 cat类似于concatenate

print("11.")
x11=torch.zeros(16).reshape(2,2,4)
y11=torch.ones(16).reshape(2,2,4)
x11_uns=x11.unsqueeze(0)
y11_uns=y11.unsqueeze(0)
z11=torch.cat((x11_uns,y11_uns),dim=0)
print(f"{x11}\n{y11}")
print(f"{z11}\n{z11.shape}")  #unsequeeze在第n维增加一维   实现高维堆叠

print("12.")
x12=torch.tensor([4,4])
y12=torch.tensor([1,1])
z12=torch.tensor([[1,1],[2,2],[3,3]])
w12=torch.tensor([[1,2],[3,4]])
print(torch.dot(x12,y12))#向量点积
print(torch.mv(z12,y12))#矩阵与向量
print(torch.mm(z12,w12))#矩阵与矩阵
print(torch.matmul(z12,w12))#同上

print("13.")
x13=torch.tensor([1.0,2,3],requires_grad=True)
y13=(x13*2).sum()
y13.backward()
print(x13.grad)
