import numpy as np
import pandas as pd

'''简单的移动平均法
data=pd.Series([533.8,574.6,606.9,649.8,705.1,772.0,816.4,892.7,963.9,1015.1,1102.7])
def calculateerror(n):
    simplemean=data.rolling(window=n).mean()  #第i个预测i+1的值
    
    S=np.sqrt(sum([(simplemean[i-1]-data[i])**2 for i in range(n,11)])/(11-n))#注意计算误差的边界取值
    return S

print(calculateerror(4))
print(calculateerror(5))#n=4时在历史值中计算误差更小
'''

#尝试指数平滑法，需要自己编写函数
data=np.array([50,52,47,51,49,48,51,40,48,52,51,59])
def e1(a):
    predicted=[51]           #取前两个数的平均值作为初始预测值
    for i in range(1,len(data+1)):
        temp=data[i-1]*a+predicted[-1]*(1-a)   #预测值=前一个预测和前一个实际不同权重相加  预测数组比观测数组多一个
        predicted.append(temp)
    return predicted
def cal(a):
    pred=e1(a)
    S=np.sqrt(sum([(pred[i]-data[i])**2 for i in range(len(data))])/len(data))#计算误差，所有实际值都有对应的预测值计算
    #print(pred)
    #print(S)
    return S
minerror=100
mina=100
x=np.linspace(0,1,20)
for i in x:
    print(cal(i))
    if (cal(i)<minerror):
        mina=i
        minerror=cal(i)
        

print(f"{mina}:{minerror}")      #看起来得到的数值很奇怪，但是也看不出什么问题

#下面我们来快速训练一个简单的神经网络来预测一下试试
import torch
import torch.nn as nn
from torch.utils.data import DataLoader,TensorDataset
from sklearn.preprocessing import StandardScaler
import torch.optim as optim

x=[[i] for i in range(1976,1987)]#Scaler只能接受np.array，不接受tensor
y=[[data[i]] for i in range(11)]
scaler=StandardScaler()
x_train=torch.tensor(scaler.fit_transform(x),dtype=torch.float32)
print(f"x_train的类型为{type(x_train)}")
x_test=torch.tensor(scaler.transform([[1987]]))
y_train=torch.tensor(scaler.fit_transform(y),dtype=torch.float32)
dataset=TensorDataset(x_train,y_train)
print(dataset)
dataload=DataLoader(dataset,batch_size=1,shuffle=False)
for input,label in dataload:
    print(f"{input}:{label}")

class Simple(nn.Module):
    def __init__(self,input_size=1,hidden_size=8,out_size=1):
        super(Simple,self).__init__()
        self.fc1=nn.Linear(input_size,hidden_size)
        self.relu=nn.ReLU()
        self.fc2=nn.Linear(hidden_size,out_size)
    
    def forward(self,x):
        out=torch.tensor(x,dtype=torch.float32)
        out=self.fc1(out)
        out=self.relu(out)
        out=self.fc2(out)
        return out
    
model=Simple()
model.train()
epoch_size=1000
criterion=nn.MSELoss()
optimizer=optim.SGD(model.parameters(),lr=0.01)
interval=max(1,epoch_size/10)
for num in range(epoch_size):
    loss_history=[]
    for input,label in dataload:
        print(type(input))
        output=model(x)
        optimizer.zero_grad()
        loss=criterion(output,label)
        loss.backward()
        optimizer.step()
    if (num+1)%interval==0:
        print(f"{num+1}/{epoch_size} finished")

pred=model(x_test)
y_p = pred.detach().numpy()
y_pred=scaler.inverse_transform(y_p)  #detach分离张量的梯度部分，从而可转化为numpy数组
print(y_pred)




